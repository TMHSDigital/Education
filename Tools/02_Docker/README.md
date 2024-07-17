# Docker

Docker is a platform designed to help developers build, share, and run applications in containers. Containers are lightweight, standalone, executable packages that include everything needed to run a piece of software, including the code, runtime, libraries, and settings.

## Why Use Docker?

- Consistency across multiple development environments
- Simplifies application deployment and scaling
- Efficient use of system resources

## Installing Docker

### Windows and macOS

1. Download Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).
2. Run the installer and follow the instructions.
3. Verify the installation by running `docker --version` in the terminal.

### Linux

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker
docker --version
```

## Basic Docker Commands

```bash
# Pull an image from Docker Hub
docker pull <image-name>

# Run a container
docker run <image-name>

# List running containers
docker ps

# Stop a running container
docker stop <container-id>

# Remove a container
docker rm <container-id>
```

