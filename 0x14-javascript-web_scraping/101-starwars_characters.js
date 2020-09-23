#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(URL, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const file = JSON.parse(body).characters;
  for (const items in file) {
    request(file[items], (err, res, body) => {
      if (err) console.log(err);
      console.log(JSON.parse(body).name);
    });
  }
});
