-- Example of Creating and Accessing Tables

-- Creating a table
fruits = {"apple", "banana", "cherry"}

-- Accessing elements
print(fruits[1])  -- Output: apple

-- Adding an element
table.insert(fruits, "orange")
print(fruits[4])  -- Output: orange

-- Iterating Tables
for i, v in ipairs(fruits) do
    print(i, v)
end

-- Using Tables as Dictionaries
person = {name = "John", age = 30}
print(person.name)  -- Output: John
print(person.age)   -- Output: 30

-- Nested Tables
matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
}

print(matrix[1][2])  -- Output: 2

