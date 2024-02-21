#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  // Check for errors
  if (error) {
    console.error(error);
    return;
  }

  // Write the response body to the specified file
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    // Check for errors while writing to file
    if (err) {
      console.error(err);
      return;
    }
    console.log(`The content has been saved to ${filePath}`);
  });
});
