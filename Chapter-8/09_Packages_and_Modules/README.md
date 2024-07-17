# Packages and Modules

Go uses packages to organize source code and modules to manage dependencies.

## Creating a Package

```go
// greetings/greetings.go
package greetings

import "fmt"

// Hello returns a greeting for the named person.
func Hello(name string) string {
    return message
}
```

## Using a Package

```go
// main.go
package main

import (
    "fmt"
    "your_project/greetings"
)

func main() {
    message := greetings.Hello("Gladys")
    fmt.Println(message)
}
```

## Managing Dependencies

Go modules are used to manage dependencies in Go projects.

```bash
go mod init your_project
go get example.com/some/package
```

