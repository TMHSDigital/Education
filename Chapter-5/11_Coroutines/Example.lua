-- Example of Coroutines

-- Creating Coroutines
co = coroutine.create(function()
    for i = 1, 5 do
        print(i)
        coroutine.yield()
    end
end)

-- Resuming Coroutines
coroutine.resume(co)  -- Output: 1
coroutine.resume(co)  -- Output: 2

-- Coroutine Status
print(coroutine.status(co))  -- Output: suspended
coroutine.resume(co)
print(coroutine.status(co))  -- Output: suspended
coroutine.resume(co)
print(coroutine.status(co))  -- Output: dead

