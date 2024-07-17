# Input and Output

## Reading from and Writing to Files

```python
# Writing to a file
with open("example.txt", "w") as file:
# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## User Input

```python
name = input("Enter your name: ")
```
