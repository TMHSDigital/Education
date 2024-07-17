// Example of Functions

package main

import "fmt"

// Defining Functions
func greet(name string) {
    fmt.Println("Hello, " + name + "!")
}

// Function Arguments
func add(a int, b int) int {
    return a + b
}

// Return Statement
func square(x int) int {
    return x * x
}

// Anonymous Functions
func main() {
    greet("World")
    fmt.Println(add(2, 3))
    result := square(4)
    fmt.Println(result)

    greet := func(name string) {
        fmt.Println("Hello, " + name + "!")
    }

    greet("John")

    // Higher-Order Functions
    apply := func(funcToApply func(int) int, value int) int {
        return funcToApply(value)
    }

    increment := func(x int) int {
        return x + 1
    }

    fmt.Println(apply(increment, 5))
}
