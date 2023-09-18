#!/usr/bin/python3
"""Defines the Rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=1):
        """Initializes a new instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate. Defaults to 0.
            y (int): The y-coordinate. Defaults to 0.
            id (int): The identifier. Defaults to None.
        """
        if x is None and y is None and id is None:
            super().__init__(id)
            self.width = width
            self.height = height
            self.x = 0
            self.y = 0
        else:
            super().__init__(id)
            self.width = width
            self.height = height
            self.x = x
            self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints to stdout the Rectangle instance with character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def integer_validator(self, name, value):
        """Validate if value is an integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    def positive_validator(self, name, value):
        """Validate if value is positive.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.
        """
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def non_negative_validator(self, name, value):
        """Validate if value is non-negative.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.
        """
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
