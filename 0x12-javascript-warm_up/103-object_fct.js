#!/usr/bin/node

// Define the myObject
const myObject = {
  type: 'object',
  value: 12
};

// Print the original myObject
console.log(myObject);

// Define the inner function in myObject
myObject.incr = function () {
  this.value++;
};

// Call incr function multiple times
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
