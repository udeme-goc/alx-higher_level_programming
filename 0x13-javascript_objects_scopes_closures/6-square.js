#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
	// Constructor takes one argument, size
	constructor(size) {
		// Call the constructor of SquareBase with size as both width and height
		super(size);
	}

	// Instance method to print the square using the character C
	charPrint(C) {
		// If C is undefined, use 'X' as the default character
		if (C === undefined) {
			C = 'X';
		}

		// Print the square using the specified character
		for (let i = 0; i < this.height; i++) {
			console.log(C.repeat(this.width));
		}
	}
}

module.exports = Square;
