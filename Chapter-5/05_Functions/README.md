# Functions

Functions in Lua are first-class values, which means they can be stored in variables, passed as arguments to other functions, and returned as values from other functions.

## Defining Functions

```lua
function greet(name)
end
```

## Function Arguments

```lua
function add(a, b)
    return a + b
end

print(add(2, 3))
```

## Return Statement

```lua
function square(x)
    return x * x
end

result = square(4)
print(result)
```

## Anonymous Functions

```lua
local function anonymous_greet(name)
end

anonymous_greet("John")
```

## Higher-Order Functions

```lua
function apply(func, value)
    return func(value)
end

function increment(x)
    return x + 1
end

print(apply(increment, 5))
```

