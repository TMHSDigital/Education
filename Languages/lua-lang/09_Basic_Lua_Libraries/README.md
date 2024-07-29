# Basic Lua Libraries

Lua provides several standard libraries for common tasks, including string manipulation, mathematical operations, and table manipulation.

## Math

```lua
print(math.sqrt(16))  -- Square root
print(math.pi)        -- Pi constant
```

## String

```lua
print(string.upper("hello"))  -- Upper case
print(string.len("hello"))    -- Length of string
```

## Table

```lua
t = {1, 2, 3}
table.insert(t, 4)
print(table.concat(t, ", "))  -- Concatenates table elements into a string
```

