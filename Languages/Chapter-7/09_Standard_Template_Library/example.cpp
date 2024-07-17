// Example of Standard Template Library

#include <iostream>
#include <vector>
#include <map>
#include <set>

int main() {
    // Using Vectors
    std::vector<int> v = {1, 2, 3, 4, 5};
    v.push_back(6);

    for (int i : v) {
        std::cout << i << std::endl;
    }

    // Using Maps
    std::map<std::string, int> age;
    age["John"] = 30;
    age["Jane"] = 25;

    for (const auto& pair : age) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    // Using Sets
    std::set<int> s = {1, 2, 3, 4, 5};
    s.insert(6);

    for (int i : s) {
        std::cout << i << std::endl;
    }

    return 0;
}

