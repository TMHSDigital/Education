// Example of Functions

#include <iostream>

// Defining Functions
void greet(std::string name) {
}

// Function Arguments
int add(int a, int b) {
    return a + b;
}

// Return Statement
int square(int x) {
    return x * x;
}

// Function Overloading
int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

int main() {
    // Using Functions
    greet("World");
    std::cout << add(2, 3) << std::endl;
    int result = square(4);
    std::cout << result << std::endl;

    // Using Function Overloading
    std::cout << add(2, 3) << std::endl;        // Calls int version
    std::cout << add(2.5, 3.5) << std::endl;    // Calls double version

    return 0;
}

