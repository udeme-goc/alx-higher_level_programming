#!/usr/bin/node
class Rectangle {
	// Constructor takes two arguments, width and height
	constructor(w, h) {
		// Checks of w or h is equal to 0 or not in a positive integer
		if (w <= 0 || h <= 0) {
			// If conditions are met, create an empty object
			return{};
		}

		// Initialize the instance attribute width with the value of w
		this.width = w;

		// Initialize the instance attribute height with the value of h
		this.height = h;
	}
}

module.exports = Rectangle;
