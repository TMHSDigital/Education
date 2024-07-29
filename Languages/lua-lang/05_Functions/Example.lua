-- Example of Defining Functions

function greet(name)
end

-- Example of Function Arguments
function add(a, b)
    return a + b
end

print(add(2, 3))

-- Example of Return Statement
function square(x)
    return x * x
end

result = square(4)
print(result)

-- Example of Anonymous Functions
local function anonymous_greet(name)
end

anonymous_greet("John")

-- Example of Higher-Order Functions
function apply(func, value)
    return func(value)
end

function increment(x)
    return x + 1
end

print(apply(increment, 5))

