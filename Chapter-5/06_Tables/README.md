# Tables

Tables are the primary data structure in Lua. They can be used as arrays, dictionaries, and more.

## Creating and Accessing Tables

```lua
-- Creating a table
fruits = {"apple", "banana", "cherry"}

-- Accessing elements
print(fruits[1])  -- Output: apple

-- Adding an element
table.insert(fruits, "orange")
print(fruits[4])  -- Output: orange
```

## Iterating Tables

```lua
for i, v in ipairs(fruits) do
    print(i, v)
end
```

## Using Tables as Dictionaries

```lua
person = {name = "John", age = 30}
print(person.name)  -- Output: John
print(person.age)   -- Output: 30
```

## Nested Tables

```lua
matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
}

print(matrix[1][2])  -- Output: 2
```

