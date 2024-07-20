# Input and Output

## Reading from and Writing to Files

```javascript
// Writing to a file (Node.js example)
const fs = require('fs');
fs.writeFileSync('example.txt', 'Hello, World!');

// Reading from a file (Node.js example)
const content = fs.readFileSync('example.txt', 'utf8');
console.log(content);
```

## User Input

```javascript
// User input (Node.js example using readline module)
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Enter your name: ', name => {
    readline.close();
});
```

