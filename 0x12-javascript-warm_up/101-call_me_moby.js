#!/usr/bin/node

// Function to execute x times a given function
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the callMeMoby function to make it visible from outside
module.exports = {
  callMeMoby
};
