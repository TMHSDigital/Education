# Control Structures

Ruby supports standard control structures such as if statements and loops.

## Conditional Statements

```ruby
x = 10
if x > 5
  puts "x is greater than 5"
elsif x == 5
  puts "x is 5"
else
  puts "x is less than 5"
end
```

## Loops

### While Loop

```ruby
count = 0
while count < 5
  puts count
  count += 1
end
```

### Until Loop

```ruby
count = 0
until count == 5
  puts count
  count += 1
end
```

### For Loop

```ruby
for i in 0..4
  puts i
end
```
