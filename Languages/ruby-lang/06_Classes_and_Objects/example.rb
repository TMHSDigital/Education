# Example of Classes and Objects

class Person
  attr_accessor :name, :age

  def initialize(name, age)
    @name = name
    @age = age
  end

  def greet
    puts "Hello, my name is \#{name} and I am \#{age} years old."
  end
end

person = Person.new("John", 30)
person.greet

# Inheritance
class Animal
  def eat
    puts "I can eat!"
  end
end

class Dog < Animal
  def bark
    puts "I can bark!"
  end
end

dog = Dog.new
dog.eat
dog.bark
