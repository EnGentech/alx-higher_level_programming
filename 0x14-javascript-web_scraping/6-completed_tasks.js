#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, _res, body) {
  if (err) {
    console.log(err);
  } else {
    const dict = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !dict[userId]) {
        dict[userId] = 0;
      }

      if (completed) ++dict[userId];
    }

    console.log(dict);
  }
});
