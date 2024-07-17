# Data Visualization

R has powerful data visualization capabilities using libraries like ggplot2.

## Basic Plot

```r
# Basic Plot
plot(1:10, main="Basic Plot", xlab="X-Axis", ylab="Y-Axis")
```

## ggplot2 Example

```r
# ggplot2 Example
library(ggplot2)

data <- data.frame(x=1:10, y=rnorm(10))
ggplot(data, aes(x=x, y=y)) + geom_point() + ggtitle("ggplot2 Example")
```

