#!/usr/bin/node

const connect = require('request');

const url = process.argv[2];

let content = connect(url, function (err, response, body) {
  content = JSON.parse(body);

  if (!err) {
    let loop;
    let count;
    let use = 0;
    const dict = {};

    for (use = 1; use <= 10; use++) {
      count = 0;
      for (loop in content) {
        if (content[loop].completed === true && content[loop].userId === use) {
          count += 1;
        }
      }
      dict[use] = count;
    }
    console.log(dict);
  }
});
