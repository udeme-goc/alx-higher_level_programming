#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(arg);

// Check if the argument is a valid positive integer
if (!isNaN(num) && num > 0) {
  // Loop to print "C is fun" x times
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
