# Inheritance and Polymorphism

Inheritance allows one class to inherit the attributes and methods of another class. Polymorphism allows methods to do different things based on the object it is acting upon.

## Inheritance

```cpp
#include <iostream>

// Base Class
class Animal {
public:
    void eat() {
    }
};

// Derived Class
class Dog : public Animal {
public:
    void bark() {
    }
};

int main() {
    Dog dog;
    dog.eat();
    dog.bark();
    return 0;
}
```

## Polymorphism

```cpp
#include <iostream>

// Base Class
class Animal {
public:
    virtual void makeSound() {
        std::cout << "Some generic animal sound" << std::endl;
    }
};

// Derived Class
class Dog : public Animal {
public:
    void makeSound() override {
        std::cout << "Bark" << std::endl;
    }
};

// Derived Class
class Cat : public Animal {
public:
    void makeSound() override {
        std::cout << "Meow" << std::endl;
    }
};

int main() {
    Animal* animal1 = new Dog();
    Animal* animal2 = new Cat();

    animal1->makeSound();  // Output: Bark
    animal2->makeSound();  // Output: Meow

    delete animal1;
    delete animal2;

    return 0;
}
```

