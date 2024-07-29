// Example of Classes and Objects
using System;

public class Person {
    public string Name;
    public int Age;

    // Constructor
    public Person(string name, int age) {
        Name = name;
        Age = age;
    }

    // Method
    public void Display() {
        Console.WriteLine("Name: " + Name + ", Age: " + Age);
    }
}

public class Example {
    public static void Main(string[] args) {
        // Creating an object
        Person person = new Person("Alice", 25);
        person.Display();
    }
}

