#!/usr/bin/node
/*
Write a function that returns the number of occurrences in a list:
Prototype: exports.nbOccurences = function (list, searchElement)
*/
exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  for (let y = 0; y < list.length; y++) {
    if (searchElement === list[y]) { x++; }
  }
  return x;
};
