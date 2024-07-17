// Example of Control Structures

#include <iostream>

int main() {
    // Conditional Statements
    int x = 10;
    if (x > 5) {
        std::cout << "x is greater than 5" << std::endl;
    } else if (x == 5) {
        std::cout << "x is 5" << std::endl;
    } else {
        std::cout << "x is less than 5" << std::endl;
    }

    // For Loop
    for (int i = 0; i < 5; ++i) {
        std::cout << i << std::endl;
    }

    // While Loop
    int count = 0;
    while (count < 5) {
        std::cout << count << std::endl;
        ++count;
    }

    // Do-While Loop
    count = 0;
    do {
        std::cout << count << std::endl;
        ++count;
    } while (count < 5);

    return 0;
}

