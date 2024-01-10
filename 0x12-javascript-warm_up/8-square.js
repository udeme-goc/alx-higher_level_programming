#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(arg);

// Check if the argument is a valid positive integer
if (!isNaN(size) && size > 0) {
  // Loop to print a square of size x
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
