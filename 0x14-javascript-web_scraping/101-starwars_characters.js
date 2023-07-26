#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

const connect = require('request');

connect(url, function (err, response, body) {
  if (!err) {
    const content = JSON.parse(body);
    const actors = content.characters;
    for (let i = 0; i <= actors.length - 1; i++) {
      const urlcharacters = actors[i];

      const newconnect = require('request');
      newconnect(urlcharacters, function (err, response, body) {
        if (!err) {
          const characterscontent = JSON.parse(body);
          console.log(characterscontent.name);
        } else {
          console.log(err);
        }
      });
    }
  } else {
    console.log(err);
  }
});
