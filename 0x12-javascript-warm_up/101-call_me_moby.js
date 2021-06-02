#!/usr/bin/node
/*
Write a function that executes x times a function.
The function must be visible from outside
Prototype: function (x, theFunction)
You are not allowed to use var
*/

export function callMeMoby (x, theFunction) {
  for (let y = 0; y < x; y++) {
    theFunction();
  }
}
