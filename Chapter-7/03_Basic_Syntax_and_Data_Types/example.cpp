// Example of Variables and Data Types

#include <iostream>
#include <string>

int main() {
    // Integer
    int x = 5;

    // Float
    float y = 3.14;

    // Double
    double z = 3.14159;

    // Character
    char c = 'A';

    // Boolean
    bool isActive = true;

    // String
    std::string name = "C++";

    // Example of Basic Operators
    int a = 10;
    int b = 5;
    std::cout << (a + b) << std::endl;  // Addition
    std::cout << (a - b) << std::endl;  // Subtraction
    std::cout << (a > b) << std::endl;  // Greater than
    std::cout << (a == b) << std::endl; // Equal to
    std::cout << (a > b && b < 10) << std::endl; // Logical AND
    std::cout << (a > b || b > 10) << std::endl;  // Logical OR

    // Example of Comments
    // This is a comment
    /* This is a
       multiline comment */

    return 0;
}

