// Example of Inheritance
public class Animal {
    public void eat() {
        System.out.println("This animal eats food.");
    }
}

public class Dog extends Animal {
    public void bark() {
        System.out.println("The dog barks.");
    }
}

// Example of Polymorphism
public class Example {
    public static void main(String[] args) {
        Animal animal = new Dog();
        animal.eat();
    }
}

