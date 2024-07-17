# Basic Syntax and Data Types

Lua uses a simple and straightforward syntax. It is dynamically typed, runs by interpreting bytecode for a register-based virtual machine, and has automatic memory management with incremental garbage collection.

## Variables and Data Types

```lua
-- Integer
x = 5

-- Float
y = 3.14

-- String
name = "Lua"

-- Boolean
isActive = true

-- Nil (similar to null)
z = nil
```

## Basic Operators

```lua
-- Arithmetic operators
a = 10
b = 5
print(a + b)  -- Addition
print(a - b)  -- Subtraction

-- Comparison operators
print(a > b)  -- Greater than
print(a == b) -- Equal to

-- Logical operators
print(a > b and b < 10) -- Logical AND
print(a > b or b > 10)  -- Logical OR
```

## Comments

```lua
-- This is a comment
--[[
This is a
multiline comment
]]
```

