# Example of Modules and Mixins

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

# Namespaces
module MathHelpers
  def self.square(x)
    x * x
  end
end

puts MathHelpers.square(4)
