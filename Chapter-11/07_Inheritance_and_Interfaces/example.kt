// Example of Inheritance

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
