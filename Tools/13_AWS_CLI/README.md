# AWS CLI

The AWS Command Line Interface (CLI) is a unified tool to manage AWS services from the command line.

## Why Use AWS CLI?

- Automates AWS service management
- Integrates with scripts and CI/CD pipelines
- Provides access to all AWS services

## Installing AWS CLI

### Windows and macOS

1. Download the AWS CLI installer from [AWS CLI's official website](https://aws.amazon.com/cli/).
2. Run the installer and follow the instructions.

### Linux

```bash
curl https://awscli.amazonaws.com/AWSCLIV2.pkg -o AWSCLIV2.pkg
sudo installer -pkg AWSCLIV2.pkg -target /
```

## Basic AWS CLI Commands

```bash
# Configure the AWS CLI
aws configure

# List S3 buckets
aws s3 ls

# Start an EC2 instance
aws ec2 start-instances --instance-ids <instance-id>

# Stop an EC2 instance
aws ec2 stop-instances --instance-ids <instance-id>
```

