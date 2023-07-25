#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(url, function (_err, _res, body) {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (Err, Res, Body) {
      console.log(JSON.parse(Body).name);
    });
  }
});
