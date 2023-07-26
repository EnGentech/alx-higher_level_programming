#!/usr/bin/node

const file = require('fs');

const content = process.argv[3];

file.writeFile(process.argv[2], content, err => {
  if (err) console.error(err);
});
