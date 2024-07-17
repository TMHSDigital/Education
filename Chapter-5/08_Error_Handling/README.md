# Error Handling

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

