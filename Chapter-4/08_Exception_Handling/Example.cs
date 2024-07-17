// Example of Exception Handling
using System;

public class Example {
    public static void Main(string[] args) {
        try {
            int result = 10 / 0;
        } catch (DivideByZeroException e) {
            Console.WriteLine("Cannot divide by zero");
        } finally {
            Console.WriteLine("This will always execute");
        }
    }
}

