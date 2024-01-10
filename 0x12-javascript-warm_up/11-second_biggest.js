#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Check if thereare no arguments or only one argument
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Convert arguments to integers and sort them in descending order
  const sortedArgs = args.map(Number).sort((a, b) => b - a);

  // Print the second biggest integer
  console.log(sortedArgs[1]);
}
