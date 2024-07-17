# Kubernetes

Kubernetes is an open-source platform designed to automate deploying, scaling, and operating application containers.

## Why Use Kubernetes?

- Manages containerized applications across multiple hosts
- Provides automated deployment and scaling
- Ensures high availability and resilience

## Installing Kubernetes

### Minikube for Local Development

1. Install Minikube from [Minikube's official website](https://minikube.sigs.k8s.io/docs/start/).
2. Start Minikube with the following command:
```bash
minikube start
```

## Basic Kubernetes Commands

```bash
# Get cluster information
kubectl cluster-info

# Get node information
kubectl get nodes

# Create a deployment
kubectl create deployment <deployment-name> --image=<image-name>

# Expose a deployment
kubectl expose deployment <deployment-name> --type=LoadBalancer --port=<port-number>

# Scale a deployment
kubectl scale deployment <deployment-name> --replicas=<number-of-replicas>
```

