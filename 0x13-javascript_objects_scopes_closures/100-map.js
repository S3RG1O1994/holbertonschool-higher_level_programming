#!/usr/bin/node

let list = require('./100-data').list;
console.log(list);
list = list.map((elm, idx) => elm * idx);
console.log(list);
