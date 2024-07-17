# Exception Handling

Kotlin provides a robust exception handling mechanism.

## Basic Exception Handling

```kotlin
fun main() {
    try {
        val result = 10 / 0
        println(result)
    } catch (e: ArithmeticException) {
        println("Cannot divide by zero")
    } finally {
        println("This will always execute")
    }
}
```
