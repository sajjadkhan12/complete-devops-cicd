# Kubernetes Manifests with Kustomize

This directory contains Kubernetes manifests organized using Kustomize for environment-specific deployments.

## Structure

```
k8s/
├── base/                    # Base manifests (no environment-specific values)
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── poem-deployment.yaml
│   ├── quote-deployment.yaml
│   ├── frontend-deployment.yaml
│   ├── ingress.yaml
│   └── kustomization.yaml
│
└── overlays/               # Environment-specific overlays
    ├── dev/
    │   ├── kustomization.yaml
    │   ├── namespace-patch.yaml
    │   └── configmap-patch.yaml
    ├── stg/
    │   ├── kustomization.yaml
    │   ├── namespace-patch.yaml
    │   └── configmap-patch.yaml
    └── prd/
        ├── kustomization.yaml
        ├── namespace-patch.yaml
        └── configmap-patch.yaml
```

## Base Manifests

The `base/` directory contains the core Kubernetes resources without environment-specific values:
- **namespace.yaml**: Base namespace definition
- **configmap.yaml**: Configuration maps for services
- **poem-deployment.yaml**: Poem service deployment and service
- **quote-deployment.yaml**: Quote service deployment and service
- **frontend-deployment.yaml**: Frontend deployment and service
- **ingress.yaml**: Ingress configuration
- **kustomization.yaml**: Kustomize base configuration

## Overlays

Each environment overlay:
- Sets the namespace (dev/stg/prd)
- Overrides image tags
- Adjusts replica counts (if needed)
- Applies environment-specific patches

## Usage

### Build manifests for an environment

```bash
# Development
kubectl kustomize k8s/overlays/dev

# Staging
kubectl kustomize k8s/overlays/stg

# Production
kubectl kustomize k8s/overlays/prd
```

### Apply manifests directly (not recommended with ArgoCD)

```bash
# Development
kubectl apply -k k8s/overlays/dev

# Staging
kubectl apply -k k8s/overlays/stg

# Production
kubectl apply -k k8s/overlays/prd
```

### Update image tags

Image tags are automatically updated by the GitHub Actions workflow. To update manually:

1. Edit `k8s/overlays/{env}/kustomization.yaml`
2. Update the `newTag` values in the `images` section
3. Commit and push changes
4. ArgoCD will automatically sync (for dev/stg) or require manual sync (prd)

## Image Configuration

Images are configured in each overlay's `kustomization.yaml`:

```yaml
images:
  - name: us-central1-docker.pkg.dev/PROJECT_ID/microservice-registery/poem-service
    newName: us-central1-docker.pkg.dev/PROJECT_ID/microservice-registery/poem-service
    newTag: latest
```

Replace `PROJECT_ID` with your actual GCP project ID.

## Environment Differences

### Development
- Namespace: `microservices-dev`
- Replicas: 2 for each service
- Auto-sync enabled in ArgoCD

### Staging
- Namespace: `microservices-stg`
- Replicas: 2 for each service
- Auto-sync enabled in ArgoCD

### Production
- Namespace: `microservices-prd`
- Replicas: 3 for each service (higher availability)
- Manual sync required in ArgoCD

## Secrets

Secrets are not managed by Kustomize. They must be created separately:

```bash
kubectl create secret generic poem-secrets \
  --from-literal=API_SECRET_KEY="value" \
  --from-literal=ADMIN_TOKEN="value" \
  -n microservices-dev
```

Or use External Secrets Operator for GitOps-based secret management.

