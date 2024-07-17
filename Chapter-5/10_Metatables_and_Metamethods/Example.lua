-- Example of Metatables and Metamethods

-- Setting a Metatable
t = {}
mt = {}
setmetatable(t, mt)

-- Metamethod: __index
mt = {
    __index = function(table, key)
        return key .. " not found"
    end
}
setmetatable(t, mt)
print(t.foo)  -- Output: foo not found

-- Metamethod: __newindex
mt = {
    __newindex = function(table, key, value)
        print(key .. " = " .. value)
    end
}
setmetatable(t, mt)
t.foo = "bar"  -- Output: foo = bar

