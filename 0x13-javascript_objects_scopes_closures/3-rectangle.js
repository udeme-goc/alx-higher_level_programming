#!/usr/bin/node
class Rectangle {
  // Constructor takes two arguments, width and height
  constructor (w, h) {
    // Checks of w or h is equal to 0 or not in a positive integer
    if (w <= 0 || h <= 0) {
      // If conditions are met, create an empty object
      return {};
    }

    // Initialize the instance attribute width with the value of w
    this.width = w;

    // Initialize the instance attribute height with the value of h
    this.height = h;
  }

  // Instance method to print the rectangle using the character 'X'
  print () {
    // Check if either width or height is 0
    if (this.width === 0 || this.height === 0) {
      // If either is 0, don't print anything
      return;
    }

    // Loop through each row
    for (let i = 0; i < this.height; i++) {
      // Print 'X' for each column
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
