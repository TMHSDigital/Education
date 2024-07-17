// Example of Control Structures

package main

import "fmt"

func main() {
    // Conditional Statements
    x := 10
    if x > 5 {
        fmt.Println("x is greater than 5")
    } else if x == 5 {
        fmt.Println("x is 5")
    } else {
        fmt.Println("x is less than 5")
    }

    // For Loop
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }

    // While Loop (simulated with for)
    count := 0
    for count < 5 {
        fmt.Println(count)
        count++
    }

    // Infinite Loop
    for {
        fmt.Println("This will loop forever")
        break // Just to prevent an actual infinite loop in this example
    }
}

