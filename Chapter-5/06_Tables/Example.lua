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

