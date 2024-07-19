# Liquid Installation and Setup

Liquid is a Ruby library, and installing it is straightforward if you have Ruby installed on your system.

## Prerequisites

- Ruby (version 2.3 or higher)
- RubyGems

## Installation Steps

1. **Install Ruby**: Follow the instructions for your operating system to install Ruby. You can download it from the official [Ruby website](https://www.ruby-lang.org/en/downloads/).

2. **Install the Liquid gem**: Open your terminal and run the following command:

    ```bash
    gem install liquid
    ```

3. **Verify Installation**: To ensure Liquid is installed correctly, run the following command in your terminal:

    ```bash
    irb -r liquid
    ```
    If you see no errors, Liquid is installed correctly.

## Using Liquid

You can use Liquid in your Ruby projects by requiring the library and creating templates. Here’s a simple example:

```ruby
require 'liquid'

# Create a Liquid template
template = Liquid::Template.parse("Hello, {{ name }}!")

# Render the template with a variable
output = template.render('name' => 'World')

puts output  # => "Hello, World!"
```

## Next Steps

After installing Liquid, you can start exploring its features and capabilities. Refer to the official [Liquid documentation](https://shopify.github.io/liquid/) for more detailed guides and tutorials.
EOF
```

### Command for PowerShell

```powershell
# Navigate to the 02_Liquid_Installation_and_Setup directory
cd /d/cloned-repo-1/Education/Languages/liquid-lang/02_Liquid_Installation_and_Setup

# Create a README.md file with installation and setup content
Add-Content -Path README.md -Value @"
# Liquid Installation and Setup

Liquid is a Ruby library, and installing it is straightforward if you have Ruby installed on your system.

## Prerequisites

- Ruby (version 2.3 or higher)
- RubyGems

## Installation Steps

1. **Install Ruby**: Follow the instructions for your operating system to install Ruby. You can download it from the official [Ruby website](https://www.ruby-lang.org/en/downloads/).

2. **Install the Liquid gem**: Open your terminal and run the following command:

    ```bash
    gem install liquid
    ```

3. **Verify Installation**: To ensure Liquid is installed correctly, run the following command in your terminal:

    ```bash
    irb -r liquid
    ```
    If you see no errors, Liquid is installed correctly.

## Using Liquid

You can use Liquid in your Ruby projects by requiring the library and creating templates. Here’s a simple example:

```ruby
require 'liquid'

# Create a Liquid template
template = Liquid::Template.parse("Hello, {{ name }}!")

# Render the template with a variable
output = template.render('name' => 'World')

puts output  # => "Hello, World!"
```

## Next Steps

After installing Liquid, you can start exploring its features and capabilities. Refer to the official [Liquid documentation](https://shopify.github.io/liquid/) for more detailed guides and tutorials.
"@
```

Please run the corrected command for your environment (Bash or PowerShell) to create the detailed installation and setup content for the `02_Liquid_Installation_and_Setup` file. Let me know once you're ready to proceed to the next file.