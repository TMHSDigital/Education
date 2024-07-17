// Example of Inheritance and Polymorphism

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

// Polymorphism
class AnimalWithSound {
public:
    virtual void makeSound() {
        std::cout << "Some generic animal sound" << std::endl;
    }
};

class DogWithSound : public AnimalWithSound {
public:
    void makeSound() override {
        std::cout << "Bark" << std::endl;
    }
};

class CatWithSound : public AnimalWithSound {
public:
    void makeSound() override {
        std::cout << "Meow" << std::endl;
    }
};

int main() {
    // Inheritance
    Dog dog;
    dog.eat();
    dog.bark();

    // Polymorphism
    AnimalWithSound* animal1 = new DogWithSound();
    AnimalWithSound* animal2 = new CatWithSound();

    animal1->makeSound();  // Output: Bark
    animal2->makeSound();  // Output: Meow

    delete animal1;
    delete animal2;

    return 0;
}

