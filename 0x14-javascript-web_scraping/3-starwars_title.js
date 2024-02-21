#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API endpoint
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API endpoint
request(apiUrl, (error, response, body) => {
  // Check for errors
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const movie = JSON.parse(body);

  // Print the title of the movie
  console.log(movie.title);
});
