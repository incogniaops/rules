# Kubernetes troubleshooting rules

## Purpose

This document defines the conventions for diagnosing and resolving issues in microservices deployed on Kubernetes with Istio.

## Methodology: outside in

Diagnosis always follows this order:

1. **Events** → detect *namespaces* and resources with failures
2. **Unstable pods** → prioritise by restart count
3. **Error patterns** → identify root cause in logs
4. **Owner** → determine the affected Deployment/StatefulSet
5. **Network** → verify Service, Endpoints, VirtualService
6. **Dependencies** → look for *cross-namespace* dependencies
7. **Fix** → propose and validate without deploying

## Diagnostic commands

### Recent events (global overview)

```bash
kubectl get events --all-namespaces --sort-by=.lastTimestamp | tail -50
```

### Pods with most restarts

```bash
kubectl get pods -A --sort-by=.status.containerStatuses[0].restartCount | tail -30
```

### Describe a problematic pod (events + owner)

```bash
kubectl describe pod -n <namespace> <pod>
```

### Logs by label (all replicas)

```bash
kubectl logs -n <namespace> -l app=<service> --since=60m --tail=500
```

### Verify Service and Endpoints

```bash
kubectl get svc,ep -n <namespace> | grep -E "<service>|<dependency>"
```

### *Cross-namespace* dependency search

```bash
# Search for a service across all namespaces
kubectl get svc -A | grep -i <dependency>
```

### Verify DNS resolution from a temporary pod

```bash
kubectl -n <namespace> run tmp --rm -it --image=busybox --restart=Never -- \
  nslookup <service>.<namespace>.svc.cluster.local
```

### Verify network connectivity

```bash
kubectl -n <namespace> run tmp --rm -it --image=busybox --restart=Never -- \
  nc -vz <service>.<namespace>.svc.cluster.local <port>
```

## Common errors

### `CrashLoopBackOff`

- Check container logs: `kubectl logs <pod> -n <namespace> --previous`
- Verify environment variables and *ConfigMaps*
- Verify that dependencies (DB, Redis, *message broker*) are reachable

### `ImagePullBackOff`

- Verify the image exists in the registry (ECR, Harbor, etc.)
- Verify registry access *secrets*: `kubectl get secret -n <namespace> | grep registry`

### Timeouts at *gateway*/ingress

- Correlate with the *backend* service: *gateway* timeouts are usually a symptom of a downstream failure
- Verify Istio VirtualService and DestinationRule

### *Cross-namespace* dependency

- If `REDIS_HOST=redis` (no FQDN), resolves to `redis.<current-namespace>.svc.cluster.local`
- Fix: use the full FQDN `redis.<real-namespace>.svc.cluster.local` or create an `ExternalName` Service

## Golden rule

**Never deploy a fix without validating the hypothesis first.** Use a temporary pod with `busybox` to verify DNS and connectivity before modifying any resource.

---

*Written by Rodrigo Álvarez (@incogniadev)*
