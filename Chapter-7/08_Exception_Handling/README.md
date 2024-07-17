# Exception Handling

C++ provides a mechanism for handling runtime errors using exceptions.

## Throwing Exceptions

```cpp
#include <iostream>

void divide(int a, int b) {
    if (b == 0) {
        throw std::invalid_argument("Cannot divide by zero");
    } else {
        std::cout << a / b << std::endl;
    }
}

int main() {
    try {
        divide(10, 0);
    } catch (const std::invalid_argument& e) {
        std::cout << e.what() << std::endl;
    }

    return 0;
}
```

## Catching Exceptions

```cpp
#include <iostream>

int main() {
    try {
        throw std::runtime_error("This is a runtime error");
    } catch (const std::runtime_error& e) {
        std::cout << e.what() << std::endl;
    }

    return 0;
}
```

## Standard Exceptions

```cpp
#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::out_of_range("Out of range error");
    } catch (const std::exception& e) {
        std::cout << e.what() << std::endl;
    }

    return 0;
}
```

