# Inheritance and Polymorphism

## Inheritance

```csharp
public class Animal {
    public void Eat() {
        Console.WriteLine("This animal eats food.");
    }
}

public class Dog : Animal {
    public void Bark() {
        Console.WriteLine("The dog barks.");
    }
}
```

## Polymorphism

```csharp
public class Example {
    public static void Main(string[] args) {
        Animal animal = new Dog();
        animal.Eat();
    }
}
```

