#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Class representing a square."""
    
    def __init__(self, size):
        """Initializes a Square instance with given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
