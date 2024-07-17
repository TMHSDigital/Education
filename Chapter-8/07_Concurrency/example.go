// Example of Concurrency

package main

import (
    "fmt"
    "time"
)

// Goroutines
func say(s string) {
    for i := 0; i < 5; i++ {
        time.Sleep(100 * time.Millisecond)
        fmt.Println(s)
    }
}

func main() {
    go say("world")
    say("hello")

    // Channels
    s := []int{7, 2, 8, -9, 4, 0}
    c := make(chan int)

    go sum(s[:len(s)/2], c)
    go sum(s[len(s)/2:], c)
    x, y := <-c, <-c

    fmt.Println(x, y, x+y)
}

// Helper function for channels example
func sum(s []int, c chan int) {
    sum := 0
    for _, v := range s {
        sum += v
    }
    c <- sum
}

