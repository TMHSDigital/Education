# Exception Handling

Ruby provides powerful built-in exception handling using the  block.

## Basic Exception Handling

```ruby
begin
  result = 10 / 0
rescue ZeroDivisionError => e
  puts "Error: \#{e.message}"
end
```

## Ensure Block

```ruby
begin
  result = 10 / 0
rescue ZeroDivisionError => e
  puts "Error: \#{e.message}"
ensure
  puts "This will always execute"
end
```
