# Helm

Helm is a package manager for Kubernetes that helps in defining, installing, and managing Kubernetes applications.

## Why Use Helm?

- Simplifies Kubernetes application deployment
- Manages application dependencies
- Supports versioning and rollback

## Installing Helm

### Windows, macOS, and Linux

1. Download Helm from [Helm's official website](https://helm.sh/docs/intro/install/).
2. Follow the installation instructions for your operating system.
3. Verify the installation by running `helm version`.

## Basic Helm Commands

```bash
# Add a Helm repository
helm repo add <repo-name> <repo-url>

# Update Helm repositories
helm repo update

# Install a Helm chart
helm install <release-name> <chart-name>

# List installed releases
helm list

# Uninstall a release
helm uninstall <release-name>
```

