# Control Structures

Lua supports standard control structures such as if statements and loops.

## Conditional Statements

```lua
x = 10
if x > 5 then
    print("x is greater than 5")
elseif x == 5 then
    print("x is 5")
else
    print("x is less than 5")
end
```

## Loops

### For Loop

```lua
for i = 0, 4 do
    print(i)
end
```

### While Loop

```lua
count = 0
while count < 5 do
    print(count)
    count = count + 1
end
```

### Repeat-Until Loop

```lua
count = 0
repeat
    print(count)
    count = count + 1
until count == 5
```

