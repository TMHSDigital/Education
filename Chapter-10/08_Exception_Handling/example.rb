# Example of Exception Handling

# Basic Exception Handling
begin
  result = 10 / 0
rescue ZeroDivisionError => e
  puts "Error: \#{e.message}"
end

# Ensure Block
begin
  result = 10 / 0
rescue ZeroDivisionError => e
  puts "Error: \#{e.message}"
ensure
  puts "This will always execute"
end
