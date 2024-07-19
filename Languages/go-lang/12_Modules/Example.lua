-- Example of Modules

-- Create a file named mymodule.lua:
-- mymodule.lua
local mymodule = {}

function mymodule.greet(name)
end

return mymodule

-- Using a Module
local mymodule = require("mymodule")
mymodule.greet("Lua")

