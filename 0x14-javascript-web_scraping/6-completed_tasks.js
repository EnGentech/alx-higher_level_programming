#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, _res, body) {
  if (err) {
    console.log(err);
  } else {
    const my_dict = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !my_dict[userId]) {
        my_dict[userId] = 0;
      }

      if (completed) ++my_dict[userId];
    }

    console.log(my_dict);
  }
});
