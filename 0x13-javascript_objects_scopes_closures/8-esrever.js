#!/usr/bin/node
/*
Write a function that returns the reversed version of a list:
Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse
*/
exports.esrever = function (list) {
  const xlist = [];
  let x = 0;

  for (x = list.length - 1; x >= 0; x--) {
    xlist.push(list[x]);
  }
  return xlist;
};
