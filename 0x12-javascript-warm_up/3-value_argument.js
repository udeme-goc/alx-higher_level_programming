#!/usr/bin/node

// Get the first argument passed to the script
const firstArg = process.argv[2];

// Check if an argument is provided and print corresponding message
if (typeof firstArg === 'undefined') {
	console.log('No argument');
} else {
	console.log(firstArg);
}
