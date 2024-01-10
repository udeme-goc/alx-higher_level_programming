#!/usr/bin/node

// Define the factorial function
function factorial (n) {
  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  }

  // Recursive case: compute factorial using recursion
  return n * factorial(n - 1);
}

// Get the argument passed to the script
const arg = parseInt(process.argv[2]);

// Check if the argument is a valid integer
if (!isNaN(arg)) {
  // Call the factorial function and print the result
  console.log(factorial(arg));
} else {
  console.log(1);
}
