# Functions

Functions in R are first-class citizens. They can be defined, assigned to variables, passed as arguments, and returned from other functions.

## Defining Functions

```r
greet <- function(name) {
}

greet("World")
```

## Function Arguments

```r
add <- function(a, b) {
  return(a + b)
}

print(add(2, 3))
```

