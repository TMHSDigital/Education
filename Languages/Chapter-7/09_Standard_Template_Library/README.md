# Standard Template Library

The Standard Template Library (STL) in C++ provides a set of common classes and interfaces for data structures and algorithms.

## Vectors

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    v.push_back(6);

    for (int i : v) {
        std::cout << i << std::endl;
    }

    return 0;
}
```

## Maps

```cpp
#include <iostream>
#include <map>

int main() {
    std::map<std::string, int> age;
    age["John"] = 30;
    age["Jane"] = 25;

    for (const auto& pair : age) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}
```

## Sets

```cpp
#include <iostream>
#include <set>

int main() {
    std::set<int> s = {1, 2, 3, 4, 5};
    s.insert(6);

    for (int i : s) {
        std::cout << i << std::endl;
    }

    return 0;
}
```

