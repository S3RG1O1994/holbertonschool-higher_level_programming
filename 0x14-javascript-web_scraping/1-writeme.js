#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

function writter (file, string) {
  const stream = fs.createWriteStream(file);
  stream.once('open', function (fd) {
    stream.write(string);
    stream.end();
  });
}

writter(file, string);
