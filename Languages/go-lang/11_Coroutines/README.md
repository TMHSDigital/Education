# Coroutines

Coroutines are a powerful feature in Lua that allows you to create functions that can pause and resume their execution.

## Creating Coroutines

```lua
co = coroutine.create(function()
    for i = 1, 5 do
        print(i)
        coroutine.yield()
    end
end)
```

## Resuming Coroutines

```lua
coroutine.resume(co)  -- Output: 1
coroutine.resume(co)  -- Output: 2
```

## Coroutine Status

```lua
print(coroutine.status(co))  -- Output: suspended
coroutine.resume(co)
print(coroutine.status(co))  -- Output: suspended
coroutine.resume(co)
print(coroutine.status(co))  -- Output: dead
```

