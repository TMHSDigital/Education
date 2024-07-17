// Example of Conditional Statements
using System;

public class Example {
    public static void Main(string[] args) {
        int x = 10;
        if (x > 5) {
            Console.WriteLine("x is greater than 5");
        } else if (x == 5) {
            Console.WriteLine("x is 5");
        } else {
            Console.WriteLine("x is less than 5");
        }

        // Example of For Loop
        for (int i = 0; i < 5; i++) {
            Console.WriteLine(i);
        }

        // Example of While Loop
        int count = 0;
        while (count < 5) {
            Console.WriteLine(count);
            count++;
        }
    }
}

