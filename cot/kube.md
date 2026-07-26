---
domain: infrastructure
task: analyse Kubernetes cluster state via SSH
dificultad: intermediate
longitud_objetivo: medium
validacion: status report covering nodes, pods, services, VirtualServices, and Istio
---
<!-- markdownlint-disable MD041 -->

Reasoning:

- Clusters run on bare-metal with Istio, ArgoCD, Prometheus, Grafana, and Kiali.
- Access is via SSH with user `ubuntu` (or other) and key `kone` (own infra) or `cad` (clients).
- Manifests are in `/home/<user>/kubernetes-<namespace>/services/`.
- Main reference: «~/rules/rulesets/KUBE.md» ([../rulesets/KUBE.md](../rulesets/KUBE.md)).

Steps:

1) Action: connect to the server via SSH.
   Result: `ssh -i ~/.ssh/<key> <user>@<ip>`
   Verify: successful connection, `kubectl` available.

2) Action: verify general cluster state.
   Result:
   - `kubectl get nodes -o wide` → all nodes in Ready state
   - `kubectl top nodes` → CPU and memory usage

3) Action: list pods in the target *namespace*.
   Result:
   - `kubectl get pods -n <namespace> -o wide`
   - Look for pods in a state other than Running/Completed
   - If there are issues: `kubectl describe pod <pod> -n <namespace>`

4) Action: review services and endpoints.
   Result:
   - `kubectl get svc -n <namespace>`
   - `kubectl get endpoints -n <namespace>`

5) Action: review VirtualServices and Istio.
   Result:
   - `kubectl get vs -n <namespace>`
   - `kubectl get gateway -n <namespace>`
   - `istioctl analyze -n <namespace>` (if available)
   - `istioctl proxy-status` (verify sidecar synchronisation)

6) Action: verify ArgoCD.
   Result:
   - `kubectl get app -n argocd | grep <namespace>`
   - Confirm Synced and Healthy state

7) Action: review recent events.
   Result:
   - `kubectl get events -n <namespace> --sort-by='.lastTimestamp' | tail -20`

8) Action: review manifests on disk.
   Result:
   - `ls /home/<user>/kubernetes-<namespace>/services/overlays/dev/`
   - `ls /home/<user>/kubernetes-<namespace>/services/base/`

9) Action: service health checks.
   Result:
   - Get Gateway IP: `kubectl get svc -n istio-system istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}'`
   - `curl -s http://<gateway_ip>/<prefix>/actuator/health`

10) Action: verify observability.
    Discover IPs and ports: `kubectl get svc -n istio-system | grep -iE 'kiali|prometheus|grafana'`
    Result:
    - Kiali: port 20001 (LoadBalancer or NodePort)
    - Prometheus: port 9090 (NodePort)
    - Grafana: port 3000 (LoadBalancer or NodePort)
    - Verify access: `curl -s -o /dev/null -w "%{http_code}" http://<ip>:<port>`

Conclusion:

- Deliver a report covering: node state, problematic pods, services and VirtualServices, ArgoCD state, recent events, and observability state.
- If there are issues, include relevant logs (`kubectl logs <pod> -n <namespace> --tail=50`).
- References: «~/rules/rulesets/KUBE.md» ([../rulesets/KUBE.md](../rulesets/KUBE.md)).
