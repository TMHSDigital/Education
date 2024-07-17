# Functions

Functions in Swift are first-class citizens. They can be assigned to variables, passed as arguments, and returned from other functions.

## Defining Functions

```swift
func greet(name: String) {
    print("Hello, \(name)!")
}

greet(name: "World")
```

## Function Arguments

```swift
func add(a: Int, b: Int) -> Int {
    return a + b
}

print(add(a: 2, b: 3))
```

## Return Statement

```swift
func square(x: Int) -> Int {
    return x * x
}

let result = square(x: 4)
print(result)
```

## Closures

```swift
let greet = { (name: String) in
    print("Hello, \(name)!")
}

greet("John")
```

## Higher-Order Functions

```swift
func apply(function: (Int) -> Int, to value: Int) -> Int {
    return function(value)
}

func increment(x: Int) -> Int {
    return x + 1
}

print(apply(function: increment, to: 5))
```
