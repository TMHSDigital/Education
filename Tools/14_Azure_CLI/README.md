# Azure CLI

The Azure Command-Line Interface (CLI) is a set of commands used to manage Azure resources from the command line.

## Why Use Azure CLI?

- Simplifies Azure resource management
- Integrates with scripts and CI/CD pipelines
- Provides access to all Azure services

## Installing Azure CLI

### Windows and macOS

1. Download the Azure CLI installer from [Azure CLI's official website](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
2. Run the installer and follow the instructions.

### Linux

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

## Basic Azure CLI Commands

```bash
# Login to Azure
az login

# List all resource groups
az group list

# Create a new resource group
az group create --name <resource-group-name> --location <location>

# Delete a resource group
az group delete --name <resource-group-name> --yes --no-wait
```

