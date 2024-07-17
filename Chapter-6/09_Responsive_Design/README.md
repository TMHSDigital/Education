# Responsive Design

Responsive web design ensures that your web pages look good on all devices. It uses flexible layouts, flexible images, and media queries.

## Media Queries

```css
/* Extra small devices (phones, less than 768px) */
@media (max-width: 767px) {
  body {
    background-color: lightblue;
  }
}

/* Small devices (tablets, 768px and up) */
@media (min-width: 768px) and (max-width: 991px) {
  body {
    background-color: lightgreen;
  }
}

/* Medium devices (desktops, 992px and up) */
@media (min-width: 992px) and (max-width: 1199px) {
  body {
    background-color: lightyellow;
  }
}

/* Large devices (large desktops, 1200px and up) */
@media (min-width: 1200px) {
  body {
    background-color: lightcoral;
  }
}
```
