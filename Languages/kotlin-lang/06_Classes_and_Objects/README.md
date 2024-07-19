# Classes and Objects

Kotlin is an object-oriented programming language. You can define classes and create objects in Kotlin.

## Defining a Class

```kotlin
class Person(val name: String, var age: Int)

fun main() {
    val person = Person("John", 30)
    println("Name: ${person.name}, Age: ${person.age}")
}
```
