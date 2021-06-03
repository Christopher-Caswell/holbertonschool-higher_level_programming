#!/usr/bin/node
/*
Write a script that computes and prints a factorial
The first argument is integer (argument can be cast as integer)
used for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function
You must use console.log(...) to print all output
You are not allowed to use var
*/

const x = process.argv[2];

function factorial (x) {
  let y = 1;

  if (x === 0 || x === 1 || isNaN(x) === true) {
    return y;
  } else {
    y = x * factorial(x - 1);
  }
  return (y);
}
if (process.argv.length < 3) {
  console.log(1);
} else {
  const z = factorial(x);
  console.log(z);
}
