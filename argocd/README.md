# ArgoCD Configuration

This directory contains ArgoCD Application manifests for GitOps-based deployment.

## Structure

- `applications/` - Individual ArgoCD Application definitions for each environment
  - `dev-application.yaml` - Development environment
  - `stg-application.yaml` - Staging environment
  - `prd-application.yaml` - Production environment
- `app-of-apps.yaml` - App of Apps pattern to manage all applications

## Setup Instructions

### 1. Update Repository URLs

Before applying, update the repository URLs in all application manifests:

```yaml
source:
  repoURL: https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
```

Replace:
- `YOUR_GITHUB_USERNAME` with your GitHub username
- `YOUR_REPO_NAME` with your repository name

### 2. Install ArgoCD (if not already installed)

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### 3. Access ArgoCD UI

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Default username: `admin`
Get password: `kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d`

### 4. Apply App of Apps Pattern

```bash
kubectl apply -f argocd/app-of-apps.yaml
```

This will automatically create all environment applications.

### 5. Or Apply Individual Applications

```bash
kubectl apply -f argocd/applications/dev-application.yaml
kubectl apply -f argocd/applications/stg-application.yaml
kubectl apply -f argocd/applications/prd-application.yaml
```

## Sync Policies

- **Dev & Staging**: Automated sync enabled (auto-deploys on Git changes)
- **Production**: Manual sync (requires approval in ArgoCD UI)

## Secret Management

Secrets need to be created manually or via External Secrets Operator. The applications expect:
- `poem-secrets` in each namespace
- `quote-secrets` in each namespace

See the GitHub Actions workflow for secret creation commands.

