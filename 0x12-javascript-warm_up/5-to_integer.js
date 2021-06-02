#!/usr/bin/node
/*
Write a script that prints My number:
<first argument converted in integer>
if the first argument can be converted to an integer:
-
If the argument can’t be converted to an integer, print “Not a number”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use try/catch
*/
const x = process.argv[2];

if (process.argv[2] === undefined) {
  console.log('Not a number');
} else if (process.argv[2] % 1 !== 0) {
  console.log('Not a number');
} else if (process.argv[2] % 1 === 0) {
  console.log('My number: ' + x);
}
