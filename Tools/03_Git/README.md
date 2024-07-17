# Git

Git is a distributed version control system that helps developers collaborate on projects and track changes in source code over time.

## Why Use Git?

- Distributed nature allows for offline work
- Strong branching and merging capabilities
- Widely adopted with extensive community support

## Installing Git

### Windows

1. Download Git for Windows from [git-scm.com](https://git-scm.com/download/win).
2. Run the installer and follow the instructions.
3. Verify the installation by running `git --version` in the command prompt.

### macOS

```bash
brew install git
git --version
```

### Linux

```bash
sudo apt-get update
sudo apt-get install git
git --version
```

## Basic Git Commands

```bash
# Clone a repository
git clone <repository-url>

# Check the status of the repository
git status

# Stage changes for commit
git add <file-name>

# Commit changes
git commit -m "commit message"

# Push changes to remote repository
git push origin <branch-name>
```

