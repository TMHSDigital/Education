// Example of Classes and Objects

#include <iostream>

// Defining a Class
class Person {
public:
    std::string name;
    int age;

    void greet() {
        std::cout << "Hello, my name is " << name << " and I am " << age << " years old." << std::endl;
    }
};

// Using Constructors and Destructors
class PersonWithConstructor {
public:
    std::string name;
    int age;

    // Constructor
    PersonWithConstructor(std::string n, int a) {
        name = n;
        age = a;
    }

    // Destructor
    ~PersonWithConstructor() {
        std::cout << name << " is being destroyed." << std::endl;
    }

    void greet() {
        std::cout << "Hello, my name is " << name << " and I am " << age << " years old." << std::endl;
    }
};

int main() {
    // Using a Class
    Person person;
    person.name = "John";
    person.age = 30;
    person.greet();

    // Using a Class with Constructor and Destructor
    PersonWithConstructor personWithConstructor("Jane", 25);
    personWithConstructor.greet();

    return 0;
}

