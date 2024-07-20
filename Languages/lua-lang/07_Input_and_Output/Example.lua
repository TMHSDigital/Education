-- Example of Reading from and Writing to Files

-- Writing to a file
file = io.open("example.txt", "w")
file:close()

-- Reading from a file
file = io.open("example.txt", "r")
content = file:read("*all")
file:close()
print(content)

-- Example of User Input
print("Enter your name:")
name = io.read()

