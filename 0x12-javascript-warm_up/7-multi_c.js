#!/usr/bin/node
const process = require('process');

const args = process.argv;
if (!isNaN(parseInt(args[2], 10))) {
  for (let item = 0; item < parseInt(args[2], 10); item += 1) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
