#!/usr/bin/node

// Function to increment and call a given function
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

// Export the addMeMaybe function to make it visible from outside
module.exports = {
  addMeMaybe
};
