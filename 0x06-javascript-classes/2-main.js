#!/usr/bin/node
const Square = require('./2-square.js');

const mySquare1 = new Square(3);
console.log(typeof (mySquare1));
console.log(mySquare1);

const mySquare2 = new Square();
console.log(typeof (mySquare2));
console.log(mySquare2);

try {
  console.log(mySquare1.size);
} catch (err) {
  console.log(err);
}

try {
  console.log(mySquare1._size);
} catch (err) {
  console.log(err);
}

try {
  const mySquare3 = new Square('3');
  console.log(typeof (mySquare3));
  console.log(mySquare3);
} catch (err) {
  console.log(err);
}

try {
  const mySquare4 = new Square(-89);
  console.log(typeof (mySquare4));
  console.log(mySquare4.size);
  console.log(mySquare4);
} catch (err) {
  console.log(err);
}
