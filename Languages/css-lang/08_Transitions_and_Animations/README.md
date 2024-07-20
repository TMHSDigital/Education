# Transitions and Animations

CSS transitions and animations provide a way to create dynamic and interactive web pages.

## Transitions

### Transition Property

```css
.box {
  width: 100px;
  height: 100px;
  background-color: blue;
  transition: background-color 2s;
}

.box:hover {
  background-color: red;
}
```

## Animations

### Keyframes

```css
@keyframes example {
  from {background-color: red;}
  to {background-color: yellow;}
}

.box {
  width: 100px;
  height: 100px;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
}
```
