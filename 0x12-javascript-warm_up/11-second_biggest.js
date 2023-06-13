#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else if (process.argv.length > 3) {
  let array = process.argv;
  array = array.slice(2).map(Number); // this is used to convert to number
  const newArray = array.sort(function (a, b) { return b - a; });
  console.log(newArray[1]);
}
