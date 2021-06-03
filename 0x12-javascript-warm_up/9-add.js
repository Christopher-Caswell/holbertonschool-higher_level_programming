#!/usr/bin/node
/*
Write a script that prints the addition of 2 integers
The first argument is the first integer
The second argument is the second integer
You have to define a function with this prototype:
function add(a, b)
You must use console.log(...) to print all output
You are not allowed to use var
*/

const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

if (process.argv.length < 4) {
  console.log('NaN');
} else {
  const res = add(a, b);
  console.log(res);
  
}
