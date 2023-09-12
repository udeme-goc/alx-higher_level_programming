#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class for representing squares.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with specified size.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string in the format '[Square] <size>/<size>'.
        """
        return "[Square] {}/{}".format(self.__width, self.__height)
