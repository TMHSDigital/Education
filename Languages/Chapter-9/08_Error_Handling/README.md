# Error Handling

Swift provides powerful built-in error handling using the  statement.

## Throwing Errors

```swift
enum DivisionError: Error {
    case divisionByZero
}

func divide(_ a: Int, by b: Int) throws -> Int {
    if b == 0 {
        throw DivisionError.divisionByZero
    }
    return a / b
}
```

## Handling Errors

```swift
do {
    let result = try divide(10, by: 0)
    print(result)
} catch DivisionError.divisionByZero {
    print("Error: Division by zero")
} catch {
    print("An unexpected error occurred: \(error)")
}
```

## Optional Try

```swift
let result = try? divide(10, by: 2)
print(result ?? "No result")
```

## Forced Try

```swift
let result = try! divide(10, by: 2)
print(result)
```
