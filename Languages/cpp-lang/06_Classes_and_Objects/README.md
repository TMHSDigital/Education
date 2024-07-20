# Classes and Objects

C++ is an object-oriented programming language, and classes and objects are fundamental to OOP in C++.

## Defining a Class

```cpp
#include <iostream>

class Person {
public:
    std::string name;
    int age;

    void greet() {
        std::cout << "Hello, my name is " << name << " and I am " << age << " years old." << std::endl;
    }
};

int main() {
    Person person;
    person.name = "John";
    person.age = 30;
    person.greet();
    return 0;
}
```

## Constructors

```cpp
#include <iostream>

class Person {
public:
    std::string name;
    int age;

    // Constructor
    Person(std::string n, int a) {
        name = n;
        age = a;
    }

    void greet() {
        std::cout << "Hello, my name is " << name << " and I am " << age << " years old." << std::endl;
    }
};

int main() {
    Person person("John", 30);
    person.greet();
    return 0;
}
```

## Destructors

```cpp
#include <iostream>

class Person {
public:
    std::string name;
    int age;

    // Constructor
    Person(std::string n, int a) {
        name = n;
        age = a;
    }

    // Destructor
    ~Person() {
        std::cout << name << " is being destroyed." << std::endl;
    }

    void greet() {
        std::cout << "Hello, my name is " << name << " and I am " << age << " years old." << std::endl;
    }
};

int main() {
    Person person("John", 30);
    person.greet();
    return 0;
}
```

