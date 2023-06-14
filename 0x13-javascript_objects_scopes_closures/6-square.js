#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
