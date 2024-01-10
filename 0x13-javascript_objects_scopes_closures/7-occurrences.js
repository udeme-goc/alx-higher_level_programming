#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Use the filter function to count occurrences
  const occurrences = list.filter(element => element === searchElement);

  // Return the count of occurences
  return occurrences.length;
};
