#!/usr/bin/node

let list = require('./100-data').list;
console.log(list);
list = list.map(x => x * (x - 1));
console.log(list);
