#!/usr/bin/node
const process = require('process');

const args = process.argv;
if (args[2]) {
  const myList = args.slice(2);
  if (myList.length > 1) {
    console.log(
      myList.sort(function (a, b) { return a - b; })[
        parseInt(myList.length - 2, 10)
      ]
    );
  } else {
    console.log(0);
  }
} else {
  console.log(0);
}
