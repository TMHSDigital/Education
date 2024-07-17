# Metatables and Metamethods

Metatables allow you to change the behavior of tables in Lua. Metamethods are the methods that a metatable can contain to define this behavior.

## Setting a Metatable

```lua
t = {}
mt = {}

setmetatable(t, mt)
```

## Metamethods

### __index

```lua
t = {}
mt = {
    __index = function(table, key)
        return key .. " not found"
    end
}

setmetatable(t, mt)
print(t.foo)  -- Output: foo not found
```

### __newindex

```lua
t = {}
mt = {
    __newindex = function(table, key, value)
        print(key .. " = " .. value)
    end
}

setmetatable(t, mt)
t.foo = "bar"  -- Output: foo = bar
```

