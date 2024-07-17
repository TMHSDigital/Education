// Example of Error Handling

enum DivisionError: Error {
    case divisionByZero
}

func divide(_ a: Int, by b: Int) throws -> Int {
    if b == 0 {
        throw DivisionError.divisionByZero
    }
    return a / b
}

// Handling Errors
do {
    let result = try divide(10, by: 0)
    print(result)
} catch DivisionError.divisionByZero {
    print("Error: Division by zero")
} catch {
    print("An unexpected error occurred: \(error)")
}

// Optional Try
let result = try? divide(10, by: 2)
print(result ?? "No result")

// Forced Try
let result = try! divide(10, by: 2)
print(result)
