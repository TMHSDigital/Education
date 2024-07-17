# Control Structures

Go supports standard control structures such as if statements and loops.

## Conditional Statements

```go
package main

import "fmt"

func main() {
    x := 10
    if x > 5 {
        fmt.Println("x is greater than 5")
    } else if x == 5 {
        fmt.Println("x is 5")
    } else {
        fmt.Println("x is less than 5")
    }
}
```

## Loops

### For Loop

```go
package main

import "fmt"

func main() {
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }
}
```

### While Loop (simulated with for)

```go
package main

import "fmt"

func main() {
    count := 0
    for count < 5 {
        fmt.Println(count)
        count++
    }
}
```

### Infinite Loop

```go
package main

import "fmt"

func main() {
    for {
        fmt.Println("This will loop forever")
    }
}
```

