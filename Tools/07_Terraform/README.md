# Terraform

Terraform is an open-source infrastructure as code (IaC) software tool created by HashiCorp. It allows users to define and provision infrastructure using a high-level configuration language.

## Why Use Terraform?

- Automates the provisioning of infrastructure
- Supports multiple cloud providers
- Enables version control for infrastructure

## Installing Terraform

### Windows, macOS, and Linux

1. Download Terraform from [Terraform's official website](https://www.terraform.io/downloads.html).
2. Extract the executable and add it to your system's PATH.
3. Verify the installation by running `terraform --version`.

## Basic Terraform Commands

```bash
# Initialize a Terraform configuration
terraform init

# Plan the changes required to reach the desired state
terraform plan

# Apply the changes to reach the desired state
terraform apply

# Destroy the Terraform-managed infrastructure
terraform destroy
```

