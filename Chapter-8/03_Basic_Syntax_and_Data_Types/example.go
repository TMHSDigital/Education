// Example of Variables and Data Types

package main

import "fmt"

func main() {
    // Integer
    var x int = 5

    // Float
    var y float64 = 3.14

    // String
    var name string = "Go"

    // Boolean
    var isActive bool = true

    // Inferred types
    z := 10
    fmt.Println(x, y, name, isActive, z)

    // Example of Basic Operators
    a := 10
    b := 5
    fmt.Println(a + b)  // Addition
    fmt.Println(a - b)  // Subtraction
    fmt.Println(a > b)  // Greater than
    fmt.Println(a == b) // Equal to
    fmt.Println(a > b && b < 10) // Logical AND
    fmt.Println(a > b || b > 10) // Logical OR

    // Example of Comments
    // This is a comment
    /*
    This is a
    multiline comment
    */
    fmt.Println("Hello, Go!")
}
