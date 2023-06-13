#!/usr/bin/node

function factorial (num) {
  if (num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const val = parseInt(process.argv[2]);
if (isNaN(val)) {
  console.log(factorial(1));
} else {
  console.log(factorial(val));
}
