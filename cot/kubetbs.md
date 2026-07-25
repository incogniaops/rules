---
domain: kubernetes
task: locate a problematic microservice by correlating logs and pods across multiple namespaces
dificultad: high
longitud_objetivo: medium
validacion: identify the affected service/deployment and list of impacted pods with time window and error pattern
---
<!-- markdownlint-disable MD041 -->

Reasoning:
- Use an outside-in traversal: recent events → unstable pods → error patterns → owner (Deployment/StatefulSet) → Service/Ingress/VirtualService.
- Maintain International English (UK) and repo CoT format (see «~/rules/rulesets/LINGUISTICS.md» ([../rulesets/LINGUISTICS.md](../rulesets/LINGUISTICS.md))).
- Main reference: «~/rules/rulesets/KUBETBS.md» ([../rulesets/KUBETBS.md](../rulesets/KUBETBS.md)).
- Use non-interactive commands and label selectors to cover all replicas.

Steps:
1) Action: list recent events to detect namespaces and resources with failures.
   Result: `kubectl get events --all-namespaces --sort-by=.lastTimestamp | tail -n 50` shows errors in the "payments" namespace (intermittent ImagePullBackOff and CrashLoopBackOff) and timeouts in "checkout".
2) Action: list pods with high restart counts to prioritise.
   Result: `kubectl get pods -A --sort-by=.status.containerStatuses[0].restartCount | tail -n 30` reveals `payments-api-xxxx` and `checkout-gw-yyyy` pods with frequent restarts.
3) Action: describe one of the high-restart pods to inspect events and owner (ownerReferences).
   Result: `kubectl describe pod -n payments payments-api-xxxx` indicates owner `Deployment/payments-api` and connection errors to `redis:6379`.
4) Action: retrieve logs from all microservice pods by label to find the common pattern.
   Result: `kubectl logs -n payments -l app=payments-api --since=60m --tail=500` repeatedly shows `ERR connection refused` towards `redis`.
5) Action: confirm the Service/Endpoints of the backend that the problematic microservice points to.
   Result: `kubectl get svc,ep -n payments | grep -E "redis|payments"` shows `svc/redis` with no endpoints (0/0), and `svc/payments-api` normal.
6) Action: verify the backend Deployment/StatefulSet (if applicable) and its pods.
   Result: `kubectl get deploy,statefulset -n payments | grep -i redis` lists no resources; `kubectl get pods -n payments -l app=redis` returns empty.
7) Action: broaden the redis search across the entire cluster (possible cross-namespace dependency) and review DNS policy.
   Result: `kubectl get svc -A | grep -i redis` reveals `redis` in the `infra` namespace. `kubectl get svc -n infra redis -o yaml` confirms `clusterIP` and selector `app=redis` with active endpoints.
8) Action: verify how the microservice resolves the `redis` hostname and whether it uses FQDN.
   Result: `kubectl get deploy -n payments payments-api -o yaml | yq '.spec.template.spec.containers[].env'` shows `REDIS_HOST=redis` (no FQDN). With the default DNS policy, `redis` resolves to `redis.payments.svc.cluster.local`, which does not exist in `payments`.
9) Action: correlate with the checkout gateway/ingress for the timeouts.
   Result: `kubectl logs -n checkout -l app=checkout-gw --since=60m --tail=500 | grep -i timeout` shows timeouts calling `http://payments-api.payments.svc.cluster.local` (matches the payments-api degradation).
10) Action: propose a minimal fix and validate the hypothesis without deploying.
    Result: use the variable `REDIS_HOST=redis.infra.svc.cluster.local` or inject an appropriate `DNS search`; verify connectivity with a temporary pod: `kubectl -n payments run tmp --rm -it --image=busybox --restart=Never -- nslookup redis.infra.svc.cluster.local && nc -vz redis.infra.svc.cluster.local 6379`.

Conclusion:
- Affected microservice: «payments-api» (Deployment in namespace «payments»); pods with restarts: `payments-api-xxxx` (and replicas).
- Root cause: `REDIS_HOST` variable points to the local `redis` in namespace «payments», but the Redis service lives in «infra». DNS/FQDN resolution failure causes `connection refused` and triggers timeouts in «checkout».
- Fix: update the config (ConfigMap/vars) to `REDIS_HOST=redis.infra.svc.cluster.local` or create a local `Service` with `ExternalName` pointing to the «infra» redis. Validate with a temporary pod before deploying.
