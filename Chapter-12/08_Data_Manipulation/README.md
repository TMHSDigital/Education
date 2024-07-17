# Data Manipulation

R provides powerful tools for data manipulation, such as dplyr.

## Using dplyr

```r
# Using dplyr
library(dplyr)

data <- data.frame(x=1:10, y=rnorm(10))
data <- data %>% filter(x > 5) %>% mutate(z = x * y)
print(data)
```
