# Control Structures

Kotlin supports standard control structures such as if statements and loops.

## Conditional Statements

```kotlin
fun main() {
    val x = 10
    if (x > 5) {
        println("x is greater than 5")
    } else if (x == 5) {
        println("x is 5")
    } else {
        println("x is less than 5")
    }
}
```

## Loops

```kotlin
fun main() {
    for (i in 1..5) {
        println(i)
    }
}
```
