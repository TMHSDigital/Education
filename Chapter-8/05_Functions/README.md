# Functions

Functions in Go are first-class citizens. They can be assigned to variables, passed as arguments, and returned from other functions.

## Defining Functions

```go
package main

import "fmt"

func greet(name string) {
}

func main() {
    greet("World")
}
```

## Function Arguments

```go
package main

import "fmt"

func add(a int, b int) int {
    return a + b
}

func main() {
    fmt.Println(add(2, 3))
}
```

## Return Statement

```go
package main

import "fmt"

func square(x int) int {
    return x * x
}

func main() {
    result := square(4)
    fmt.Println(result)
}
```

## Anonymous Functions

```go
package main

import "fmt"

func main() {
    greet := func(name string) {
    }

    greet("John")
}
```

## Higher-Order Functions

```go
package main

import "fmt"

func apply(funcToApply func(int) int, value int) int {
    return funcToApply(value)
}

func increment(x int) int {
    return x + 1
}

func main() {
    fmt.Println(apply(increment, 5))
}
```

