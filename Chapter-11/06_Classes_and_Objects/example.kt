// Example of Defining a Class and Creating Objects

class Person(val name: String, var age: Int)

fun main() {
    val person = Person("John", 30)
    println("Name: ${person.name}, Age: ${person.age}")
}
