// Example of Writing to a File (Node.js)
const fs = require('fs');
fs.writeFileSync('example.txt', 'Hello, World!');

// Example of Reading from a File (Node.js)
const content = fs.readFileSync('example.txt', 'utf8');
console.log(content);

// Example of User Input (Node.js)
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Enter your name: ', name => {
    readline.close();
});

