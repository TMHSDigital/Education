# Google Cloud SDK

The Google Cloud SDK is a set of tools that you can use to manage resources and applications hosted on Google Cloud.

## Why Use Google Cloud SDK?

- Command-line access to Google Cloud resources
- Integration with Google Cloud services
- Automation of Google Cloud tasks

## Installing Google Cloud SDK

### Windows, macOS, and Linux

1. Download the Google Cloud SDK installer from [Google Cloud's official website](https://cloud.google.com/sdk/docs/install).
2. Follow the installation instructions for your operating system.
3. Verify the installation by running `gcloud --version`.

## Basic Google Cloud SDK Commands

```bash
# Initialize the SDK
gcloud init

# List all projects
gcloud projects list

# Set the active project
gcloud config set project <project-id>

# Deploy an application
gcloud app deploy
```

