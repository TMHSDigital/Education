# Basic Syntax and Data Types

Go has a clean and straightforward syntax. It supports a variety of data types and basic operators.

## Variables and Data Types

```go
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
}
```

## Basic Operators

```go
package main

import "fmt"

func main() {
    a := 10
    b := 5

    // Arithmetic operators
    fmt.Println(a + b)  // Addition
    fmt.Println(a - b)  // Subtraction

    // Comparison operators
    fmt.Println(a > b)  // Greater than
    fmt.Println(a == b) // Equal to

    // Logical operators
    fmt.Println(a > b && b < 10) // Logical AND
    fmt.Println(a > b || b > 10) // Logical OR
}
```

## Comments

```go
package main

import "fmt"

func main() {
    // This is a comment
    /*
    This is a
    multiline comment
    */
    fmt.Println("Hello, Go!")
}
```
