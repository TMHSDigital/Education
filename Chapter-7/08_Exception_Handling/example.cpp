// Example of Exception Handling

#include <iostream>
#include <stdexcept>

// Throwing Exceptions
void divide(int a, int b) {
    if (b == 0) {
        throw std::invalid_argument("Cannot divide by zero");
    } else {
        std::cout << a / b << std::endl;
    }
}

int main() {
    // Catching Exceptions
    try {
        divide(10, 0);
    } catch (const std::invalid_argument& e) {
        std::cout << e.what() << std::endl;
    }

    // Standard Exceptions
    try {
        throw std::out_of_range("Out of range error");
    } catch (const std::exception& e) {
        std::cout << e.what() << std::endl;
    }

    return 0;
}

