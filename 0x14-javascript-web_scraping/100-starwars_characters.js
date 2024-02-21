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

  // Fetch characters for the movie
  const charactersUrls = movie.characters;

  // Create a function to fetch character names
  const getCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  };

  // Array to store promises for fetching character names
  const characterPromises = charactersUrls.map(getCharacterName);

  // Resolve all promises
  Promise.all(characterPromises)
    .then((characterNames) => {
      // Print character names
      characterNames.forEach((name) => console.log(name));
    })
    .catch((error) => {
      console.error(error);
    });
});
