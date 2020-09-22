#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
request(URL, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const file = JSON.parse(body);
  const newDict = {};
  for (const items in file) {
    if (file[items].completed) {
      if (newDict[file[items].userId]) {
        newDict[file[items].userId]++;
      } else {
        newDict[file[items].userId] = 1;
      }
    }
  }
  console.log(newDict);
});
