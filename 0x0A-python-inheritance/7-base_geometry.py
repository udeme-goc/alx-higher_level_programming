#!/usr/bin/python3
"""
Module extends the BaseGeometry class to include an integer validator method.
"""


class BaseGeometry:
    """
    A base class for geometry operations.
    """

    def area(self):
        """
        Calculate the area (not implemented).
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
