#!/usr/bin/node

// Import the fs (file system) module
const fs = require('fs');

// Get the file path from the command-line arguments
const filePath = process.argv[2];

// Read the contents of the file asynchronously
fs.readFile(filePath, 'utf-8', (err, data) => {
  // Check if there is an error
  if (err) {
    // If there is an error, print the error object
    console.error(err);
    return;
  }
  // If there is no error, print the content of the file
  console.log(data);
});
