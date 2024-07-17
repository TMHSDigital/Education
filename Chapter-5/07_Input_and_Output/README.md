# Input and Output

## Reading from and Writing to Files

```lua
-- Writing to a file
file = io.open("example.txt", "w")
file:close()

-- Reading from a file
file = io.open("example.txt", "r")
content = file:read("*all")
file:close()
print(content)
```

## User Input

```lua
print("Enter your name:")
name = io.read()
```

