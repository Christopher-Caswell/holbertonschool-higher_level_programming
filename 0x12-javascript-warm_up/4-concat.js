#!/usr/bin/node
/*
Write a script that prints two arguments passed to it,
in the following format: “ is ”
-
You must use console.log(...) to print all output
You are not allowed to use var
*/
const x = process.argv[2];
const y = process.argv[3];

if (process.argv[2] === undefined) {
  console.log(undefined + ' is ' + undefined);
} else {
  console.log(x + ' is ' + y);
}
