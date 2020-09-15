#!/usr/bin/node
const process = require('process');

const args = process.argv;
function factorial (num) {
  if (isNaN(num)) {
    return(1);
  } else if (num < 0) {
    return(-1);
  } else if (num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}

console.log(factorial(parseInt(args[2])));

