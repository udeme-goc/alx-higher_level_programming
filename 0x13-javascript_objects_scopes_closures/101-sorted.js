#!/usr/bin/node

const { dict } = require('./101-data');

// Function to invert the original dictionary
function invertDictionary (originalDict) {
  const invertedDict = {};

  for (const userId in originalDict) {
    const occurrences = originalDict[userId];

    // If the occurrences is not a key in the inverted dictionary, create an empty array
    if (!invertedDict[occurrences]) {
      invertedDict[occurrences] = [];
    }

    // Push the user id to the list associated with the occurrences key
    invertedDict[occurrences].push(userId);
  }

  return invertedDict;
}

// Use the function to invert the original dictionary
const sortedDict = invertDictionary(dict);

// Print the new dictionary
console.log(sortedDict);
