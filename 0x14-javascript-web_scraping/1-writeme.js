#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the file asynchronously
fs.writeFile(filePath, content, 'utf-8', (err) => {
  // Check if there is an error
  if (err) {
    // If there is an error, print the error object
    console.error(err);
  }
});
