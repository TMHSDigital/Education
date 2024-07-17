# Modules

Modules in Lua are a way to organize and reuse code. They are typically stored in separate files and can be included using the `require` function.

## Creating a Module

Create a file named `mymodule.lua`:

```lua
-- mymodule.lua
local mymodule = {}

function mymodule.greet(name)
end

return mymodule
```

## Using a Module

```lua
local mymodule = require("mymodule")
mymodule.greet("Lua")
```

