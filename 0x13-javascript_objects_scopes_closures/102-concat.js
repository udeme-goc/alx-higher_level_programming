#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

// Extract file paths from command-line arguments
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

// Read the contents of the first source file
fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
  if (err1) {
    console.error(err1.message);
    process.exit(1);
  }

  // Read the contents of the second source file
  fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
    if (err2) {
      console.error(err2.message);
      process.exit(1);
    }

    // Concatenate the contents of the two source files
    const concatenatedData = data1 + data2;

    // Write the result to the destination file
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err3) => {
      if (err3) {
        console.error(err3.message);
        process.exit(1);
      }

      console.log(`Concatenation successful! Result written to ${destinationFile}`);
    });
  });
});
