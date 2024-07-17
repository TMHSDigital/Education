# Error Handling

Lua provides mechanisms for handling errors and exceptions using the `error` function and the `pcall` and `xpcall` functions.

## Using pcall

```lua
function divide(a, b)
    if b == 0 then
        error("Cannot divide by zero")
    else
        return a / b
    end
end

status, result = pcall(divide, 10, 0)
if status then
    print(result)
else
    print(result)
end
```

## Using xpcall

```lua
function divide(a, b)
    if b == 0 then
        error("Cannot divide by zero")
    else
        return a / b
    end
end

function errorHandler(err)
    print("Error: " .. err)
end

status, result = xpcall(divide, errorHandler, 10, 0)
if status then
    print(result)
end
```

