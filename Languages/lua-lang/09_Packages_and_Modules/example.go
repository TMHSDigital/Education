// Example of Packages and Modules

package main

import (
    "fmt"
    "your_project/greetings"
)

// Using a Package
func main() {
    message := greetings.Hello("Gladys")
    fmt.Println(message)
}

// greetings/greetings.go (create this file in the greetings directory)
package greetings

import "fmt"

// Hello returns a greeting for the named person.
func Hello(name string) string {
    message := fmt.Sprintf("Hi, %v. Welcome!", name)
    return message
}
