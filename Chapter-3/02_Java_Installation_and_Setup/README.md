# Java Installation and Setup

## Installing Java Development Kit (JDK)

### Windows

1. Download the JDK from [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html).
2. Run the installer and follow the prompts.
3. Set the JAVA_HOME environment variable to point to the JDK installation directory.
4. Add the JDK's `bin` directory to the PATH environment variable.
5. Verify installation by running `java -version` and `javac -version` in the command prompt.

### macOS

1. Download the JDK from [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html).
2. Run the installer and follow the prompts.
3. Set the JAVA_HOME environment variable by adding `export JAVA_HOME=$(/usr/libexec/java_home)` to your shell profile.
4. Verify installation by running `java -version` and `javac -version` in the terminal.

### Linux

```bash
sudo apt update
sudo apt install openjdk-11-jdk
java -version
javac -version
```

## Setting up an IDE

### IntelliJ IDEA

1. Download and install IntelliJ IDEA from [jetbrains.com](https://www.jetbrains.com/idea/download/).
2. Follow the setup wizard to configure the JDK.

### Eclipse

1. Download and install Eclipse from [eclipse.org](https://www.eclipse.org/downloads/).
2. Follow the setup wizard to configure the JDK.

