#!/usr/bin/node

// Require the addMeMaybe function from the 102-add_me_maybe.js file
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;

// Use the addMeMaybe function to increment and call a function
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
