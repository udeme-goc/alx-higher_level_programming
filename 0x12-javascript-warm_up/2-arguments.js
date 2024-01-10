#!/usr/bin/node

// Get the number of arguments
const numArgs = process.argv.length;

// Check number of arguments and print corresponding message
if (numArgs === 2) {
  console.log('No argument');
} else if (numArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
