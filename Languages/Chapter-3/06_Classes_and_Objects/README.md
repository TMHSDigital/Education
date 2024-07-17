# Classes and Objects

## Defining Classes

```java
public class Person {
    String name;
    int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method
    public void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}
```

## Creating Objects

```java
public class Example {
    public static void main(String[] args) {
        // Creating an object
        Person person = new Person("Alice", 25);
        person.display();
    }
}
```
