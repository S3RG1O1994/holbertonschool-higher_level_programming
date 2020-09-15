#!/usr/bin/node
const process = require('process');

const args = process.argv;
const num = parseInt(args[2], 10);
if (!isNaN(num)) {
  for (let item = 0; item < num; item += 1) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
