# Kubernetes cluster analysis rules

## Purpose

This document defines the conventions for analysing the state of Kubernetes clusters deployed on *bare-metal* with Istio, Kiali, Prometheus, and Grafana.

## Cluster access

### SSH connection

- **User**: typically `ubuntu` (may vary)
- **SSH keys**: `kone` (own infrastructure) or `cad` (client servers)
- **Command**: `ssh -i ~/.ssh/<key> <user>@<ip>`

### Manifest structure on the server

Manifests are organised by *namespace*/project under the user's `$HOME`:

```
/home/<user>/kubernetes-<namespace>/
├── services/
│   ├── base/                    # Base resources (Istio VirtualServices)
│   │   ├── virtualservice.yaml
│   │   └── gateway.yaml
│   └── overlays/
│       └── dev/                 # Development overlay (Deployments, Services, ConfigMaps)
│           ├── deployment.yaml
│           ├── service.yaml
│           ├── configmap.yaml
│           └── kustomization.yaml
```

### Stack tools

- **Kubernetes**: kubeadm, containerd
- **Service mesh**: Istio (VirtualServices, Gateway, mTLS)
- **Observability**: Kiali (mesh), Prometheus (metrics), Grafana (dashboards)
- **GitOps**: ArgoCD (automatic synchronisation)
- **CI/CD**: Jenkins (build pipelines)
- **Registry**: AWS ECR (Docker images)

## Essential diagnostic commands

### Overall cluster state

```bash
kubectl get nodes -o wide
kubectl get pods -n <namespace> -o wide
kubectl get svc -n <namespace>
kubectl get vs -n <namespace>            # Istio VirtualServices
kubectl get dr -n <namespace>            # Istio DestinationRules
```

### State of a specific service

```bash
kubectl describe pod <pod> -n <namespace>
kubectl logs <pod> -n <namespace> --tail=50
kubectl get events -n <namespace> --sort-by='.lastTimestamp' | tail -20
```

### Health checks

```bash
# Health check via Istio Gateway
curl -s http://<gateway_ip>/<prefix>/actuator/health

# Verify ArgoCD has the service synchronised
kubectl get app -n argocd | grep <service>
```

### Networking and Istio

```bash
kubectl get gateway -n <namespace>
kubectl get virtualservice -n <namespace> -o yaml
istioctl analyze -n <namespace>
istioctl proxy-status
```

### Resources and metrics

```bash
kubectl top nodes
kubectl top pods -n <namespace>
```

## Common ports and URLs

- **Istio Gateway**: port 80/443 on the load balancer IP (MetalLB)
- **Kiali**: port 20001 (LoadBalancer or NodePort 30871). Also exposes 9090 (internal metrics)
- **Prometheus**: port 9090 (NodePort 31570)
- **Grafana**: port 3000 (LoadBalancer or NodePort 32716)
- **Jenkins**: `http://<ip>:8080/jenkins`
- **ArgoCD**: `https://<ip>:30443` or `http://<ip>:30080`

### How to obtain real IPs and ports

```bash
kubectl get svc -n istio-system | grep -iE 'kiali|prometheus|grafana'
```

## Naming conventions

- *Namespace*: project or environment name (e.g. `stab`, `produccion`, `qa`)
- Services: `<service-name>` (e.g. `kabat-authorization-service`)
- Istio prefixes: `/<prefix>` with no trailing slash (e.g. `/kabat-auth`)
- Manifests: directory `kubernetes-<namespace>/`

---

*Written by Rodrigo Álvarez (@incogniadev)*
