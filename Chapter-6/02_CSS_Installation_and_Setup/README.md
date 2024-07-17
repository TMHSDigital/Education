# CSS Installation and Setup

CSS is a language that can be directly embedded in HTML documents or included as an external stylesheet. There is no need for a specific installation.

## Using CSS in HTML

### Inline CSS

```html
<html>
<head>
<title>Inline CSS</title>
</head>
<body>

<h1 style="color:blue;">This is a Blue Heading</h1>

</body>
</html>
```

### Internal CSS

```html
<html>
<head>
<title>Internal CSS</title>
<style>
h1 {
  color: blue;
}
</style>
</head>
<body>

<h1>This is a Blue Heading</h1>

</body>
</html>
```

### External CSS

Create an HTML file and link it to an external CSS file.

```html
<html>
<head>
<title>External CSS</title>
<link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>

<h1>This is a Blue Heading</h1>

</body>
</html>
```

Create a separate CSS file (styles.css):

```css
/* styles.css */
h1 {
  color: blue;
}
```

