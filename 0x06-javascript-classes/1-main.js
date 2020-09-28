#!/usr/bin/node
const MySquare = require('./1-square.js');

const square = new MySquare(3);
console.log(typeof (square));
console.log(square);

try {
  console.log(square.size);
} catch (err) {
  console.log(err);
}

try {
  console.log(square._size);
} catch (err) {
  console.log(err);
}
