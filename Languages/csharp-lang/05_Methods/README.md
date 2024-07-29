# Methods

## Defining Methods

```csharp
public class Example {
    public static void Greet(string name) {
    }
}
```

## Method Arguments

```csharp
public class Example {
    public static int Add(int a, int b) {
        return a + b;
    }

    public static void Main(string[] args) {
        Console.WriteLine(Add(2, 3));
    }
}
```

## Return Statement

```csharp
public class Example {
    public static int Square(int x) {
        return x * x;
    }

    public static void Main(string[] args) {
        int result = Square(4);
        Console.WriteLine(result);
    }
}
```

