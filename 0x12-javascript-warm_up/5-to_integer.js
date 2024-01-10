#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an iinteger
const num = parseInt(arg);

// Check if the argument is a valid integer and print the corresponding message
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
