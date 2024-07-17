// Example of Error Handling

package main

import (
    "errors"
    "fmt"
)

// Basic Error Handling
func divide(a, b int) (int, error) {
    if b == 0 {
        return 0, errors.New("Cannot divide by zero")
    }
    return a / b, nil
}

func main() {
    result, err := divide(10, 0)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Result:", result)
    }

    // Using Panic and Recover
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered from", r)
        }
    }()

    fmt.Println("Starting the program...")
    fmt.Println("This will not be printed.")
}

