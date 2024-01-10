#!/usr/bin/node

exports.converter = function (base) {
  // Return a function that converts a decimal number to specified base
  return function (decimalNumber) {
    // Use the toString method with the specified base
    return decimalNumber.toString(base);
  };
};
