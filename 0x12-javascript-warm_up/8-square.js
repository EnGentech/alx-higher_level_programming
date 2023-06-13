#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const input = parseInt(process.argv[2]);
  for (let i = 0; i < input; i++) {
    console.log('x'.repeat(input));
  }
}
