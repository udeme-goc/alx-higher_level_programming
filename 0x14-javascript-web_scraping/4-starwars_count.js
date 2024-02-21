#!/usr/bin/node

const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Wedge Antilles character ID
const wedgeAntillesId = '18';

// Make a GET request to the Star Wars API endpoint
request(apiUrl, (error, response, body) => {
  // Check for errors
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const films = JSON.parse(body).results;

  // Count the number of films where Wedge Antilles is present
  const count = films.reduce((total, film) => {
    // Check if Wedge Antilles is present in the characters list
    if (film.characters.includes(`${apiUrl}${wedgeAntillesId}/`)) {
      return total + 1;
    }
    return total;
  }, 0);

  // Print the count
  console.log(count);
});
