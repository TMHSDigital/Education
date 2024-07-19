# Modules and Mixins

Modules in Ruby are a way to group reusable code into a single unit. They can be used as namespaces or mixins.

## Defining a Module

```ruby
module Greetable
  def greet
    puts "Hello!"
  end
end

class Person
  include Greetable
end

person = Person.new
person.greet
```

## Namespaces

```ruby
module MathHelpers
  def self.square(x)
    x * x
  end
end

puts MathHelpers.square(4)
```
