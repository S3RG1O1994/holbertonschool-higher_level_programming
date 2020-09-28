#!/usr/bin/node
const Square = require('./3-square.js');

const mySquare1 = new Square(3);
console.log(`Area: ${mySquare1.area()}`);

try {
  console.log(Square.size);
} catch (err) {
  console.log(err);
}

try {
  console.log(Square._size);
} catch (err) {
  console.log(err);
}

const mySquare2 = new Square(5);
console.log(`Area: ${mySquare2.area()}`);
