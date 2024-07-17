// Example of Functions

// Defining Functions
func greet(name: String) {
    print("Hello, \(name)!")
}

// Function Arguments
func add(a: Int, b: Int) -> Int {
    return a + b
}

// Return Statement
func square(x: Int) -> Int {
    return x * x
}

// Closures
let greet = { (name: String) in
    print("Hello, \(name)!")
}

greet("John")

// Higher-Order Functions
func apply(function: (Int) -> Int, to value: Int) -> Int {
    return function(value)
}

func increment(x: Int) -> Int {
    return x + 1
}

print(apply(function: increment, to: 5))
