#!/usr/bin/node

const Square = require('./5-square.js');

const mySquare = new Square(3);
mySquare.print();

console.log('--');

mySquare.size = 10;
mySquare.print();

console.log('--');

mySquare.size = 0;
mySquare.print();

console.log('--');
