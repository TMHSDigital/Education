# Python Installation and Setup

## Installing Python

### Windows

1. Download Python from [python.org](https://www.python.org/downloads/windows/).
2. Run the installer and follow the prompts.
3. Verify installation by running `python --version` in the command prompt.

### macOS

1. Download Python from [python.org](https://www.python.org/downloads/mac-osx/).
2. Run the installer and follow the prompts.
3. Verify installation by running `python3 --version` in the terminal.

### Linux

```bash
sudo apt-get update
sudo apt-get install python3
python3 --version
```

## Setting up an IDE

### Visual Studio Code

1. Download and install VSCode from [code.visualstudio.com](https://code.visualstudio.com/).
2. Install the Python extension from the Extensions marketplace.

### PyCharm

1. Download and install PyCharm from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/).
2. Follow the setup wizard to configure Python interpreter.

## Virtual Environments

Creating and activating a virtual environment:

```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
```
