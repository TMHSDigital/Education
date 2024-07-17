-- Example of Error Handling

function divide(a, b)
    if b == 0 then
        error("Cannot divide by zero")
    else
        return a / b
    end
end

-- Using pcall
status, result = pcall(divide, 10, 0)
if status then
    print(result)
else
    print(result)
end

-- Using xpcall
function errorHandler(err)
    print("Error: " .. err)
end

status, result = xpcall(divide, errorHandler, 10, 0)
if status then
    print(result)
end

