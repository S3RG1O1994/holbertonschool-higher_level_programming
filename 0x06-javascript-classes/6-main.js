#!/usr/bin/node

const Square = require('./6-square.js');

const mySquare1 = new Square(3);
mySquare1.print();

console.log('--');
const mySquare2 = new Square(3, [1, 1]);
mySquare2.print();

console.log('--');

const mySquare3 = new Square(3, [3, 0]);
mySquare3.print();

console.log('--');
