# Functions

Functions in C++ are used to encapsulate code for reusability and modularity.

## Defining Functions

```cpp
#include <iostream>

void greet(std::string name) {
}

int main() {
    greet("World");
    return 0;
}
```

## Function Arguments

```cpp
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    std::cout << add(2, 3) << std::endl;
    return 0;
}
```

## Return Statement

```cpp
#include <iostream>

int square(int x) {
    return x * x;
}

int main() {
    int result = square(4);
    std::cout << result << std::endl;
    return 0;
}
```

## Function Overloading

```cpp
#include <iostream>

int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

int main() {
    std::cout << add(2, 3) << std::endl;        // Calls int version
    std::cout << add(2.5, 3.5) << std::endl;    // Calls double version
    return 0;
}
```

