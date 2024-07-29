# Statistical Analysis

R is widely used for statistical analysis.

## Basic Statistics

```r
# Basic Statistics
data <- c(1, 2, 3, 4, 5)
mean(data)
median(data)
sd(data)
```

## Linear Regression

```r
# Linear Regression
data <- data.frame(x=1:10, y=rnorm(10))
model <- lm(y ~ x, data=data)
summary(model)
```
