# Functions

Kotlin functions are first-class citizens. They can be assigned to variables, passed as arguments, and returned from other functions.

## Defining Functions

```kotlin
fun greet(name: String) {
}

fun main() {
    greet("World")
}
```

## Function Arguments

```kotlin
fun add(a: Int, b: Int): Int {
    return a + b
}

fun main() {
    println(add(2, 3))
}
```
