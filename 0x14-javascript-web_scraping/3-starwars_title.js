#!/usr/bin/node

const connect = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

connect(url, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
