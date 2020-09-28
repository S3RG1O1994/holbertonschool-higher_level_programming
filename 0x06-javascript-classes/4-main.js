#!/usr/bin/node
const Square = require('./4-square.js');

const mySquare = new Square(89);
console.log(`Area: ${mySquare.area()} for size: ${mySquare.size}`);

mySquare.size = 3;
console.log(`Area: ${mySquare.area()} for size: ${mySquare.size}`);

try {
	mySquare.size = '5 feet'
	console.log(`Area: ${mySquare.area()} for size: ${mySquare.size}`);
} catch(err) {
	console.log(err);
}