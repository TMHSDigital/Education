// Example of Classes and Objects

class Person {
    var name: String
    var age: Int

    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }

    func greet() {
        print("Hello, my name is \(name) and I am \(age) years old.")
    }
}

let person = Person(name: "John", age: 30)
person.greet()

// Inheritance
class Animal {
    func eat() {
        print("I can eat!")
    }
}

class Dog: Animal {
    func bark() {
        print("I can bark!")
    }
}

let dog = Dog()
dog.eat()
dog.bark()
