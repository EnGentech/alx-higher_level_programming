#!/usr/bin/node
const file = require('./100-data').list;

console.log(file);
console.log(file.map((values, index) => values * index));
