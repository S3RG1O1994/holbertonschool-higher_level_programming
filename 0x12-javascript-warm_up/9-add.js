#!/usr/bin/node
const process = require('process');

const args = process.argv;
function add (a, b) {
  console.log(parseInt(a, 10) + parseInt(b, 10));
}
add(args[2], args[3]);
