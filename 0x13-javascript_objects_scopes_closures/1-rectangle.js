#!/usr/bin/node
class Rectangle {
  // Constructor takes two arguments, width and height
  constructor (w, h) {
    // Initialize the instance attribute, width with value of w
    this.width = w;

    // Initialize the instance attribute height with the value of h
    // If height is not provided,it defaults to undefined
    this.height = h;
  }
}

module.exports = Rectangle;
