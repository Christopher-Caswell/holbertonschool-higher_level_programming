#!/usr/bin/node
/*
Update this script by adding a new function incr
that increments the integer value.
-
You are not allowed to use var
-
The script:
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
"""
YOUR CODE HERE
"""
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
*/

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () { myObject.value++; };
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
