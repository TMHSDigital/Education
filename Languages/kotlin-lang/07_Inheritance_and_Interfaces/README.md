# Inheritance and Interfaces

Kotlin supports both inheritance and interfaces.

## Inheritance

```kotlin
open class Animal(val name: String) {
    open fun sound() {
        println("Animal sound")
    }
}

class Dog(name: String): Animal(name) {
    override fun sound() {
        println("Bark")
    }
}

fun main() {
    val dog = Dog("Rex")
    dog.sound()
}
```
