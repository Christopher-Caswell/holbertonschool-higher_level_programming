#!/usr/bin/node
/*
Write a script that prints a square
The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
You must use the character X to print the square
You must use console.log(...) to print all output
You are not allowed to use var
You must use a loop (while, for, etc.)
*/

const z = process.argv[2];
const x = 'X';
let y;

if (process.argv[2] % 1 !== 0) {
  console.log('Missing size');
} else {
    for (y = 0; y <= z - 1; y++) {
    console.log(x.repeat(z));
  }
}
