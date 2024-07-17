# Ansible

Ansible is an open-source automation tool for IT tasks such as configuration management, application deployment, and provisioning.

## Why Use Ansible?

- Agentless architecture
- Simple, YAML-based configuration
- Scalable and efficient

## Installing Ansible

### Windows

1. Install Windows Subsystem for Linux (WSL).
2. Install Ansible using the package manager of your chosen Linux distribution.

### macOS

```bash
brew install ansible
```

### Linux

```bash
sudo apt-get update
sudo apt-get install ansible
```

## Basic Ansible Commands

```bash
# Check the Ansible version
ansible --version

# Run an Ansible playbook
ansible-playbook <playbook.yml>

# List available modules
ansible-doc -l
```

