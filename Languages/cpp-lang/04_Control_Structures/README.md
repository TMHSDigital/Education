# Control Structures

C++ supports standard control structures such as if statements and loops.

## Conditional Statements

```cpp
int x = 10;
if (x > 5) {
    std::cout << "x is greater than 5" << std::endl;
} else if (x == 5) {
    std::cout << "x is 5" << std::endl;
} else {
    std::cout << "x is less than 5" << std::endl;
}
```

## Loops

### For Loop

```cpp
for (int i = 0; i < 5; ++i) {
    std::cout << i << std::endl;
}
```

### While Loop

```cpp
int count = 0;
while (count < 5) {
    std::cout << count << std::endl;
    ++count;
}
```

### Do-While Loop

```cpp
int count = 0;
do {
    std::cout << count << std::endl;
    ++count;
} while (count < 5);
```

