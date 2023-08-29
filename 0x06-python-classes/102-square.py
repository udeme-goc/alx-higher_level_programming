#!/usr/bin/python3

class Square:
    """
    This is the Square class documentation.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size
    
    @property
    def size(self):
        """
        Retrieves the value of the size attribute.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Sets the value of the size attribute.

        Args:
            value: The new size value.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """
        Computes the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2
    
    def __lt__(self, other):
        """
        Less than comparison operator.

        Args:
            other: The other Square object.

        Returns:
            bool: True if self's area is less than other's area, False otherwise.
        """
        return self.area() < other.area()
    
    def __le__(self, other):
        """
        Less than or equal comparison operator.

        Args:
            other: The other Square object.

        Returns:
            bool: True if self's area is less than or equal to other's area, False otherwise.
        """
        return self.area() <= other.area()
    
    def __eq__(self, other):
        """
        Equal comparison operator.

        Args:
            other: The other Square object.

        Returns:
            bool: True if self's area is equal to other's area, False otherwise.
        """
        return self.area() == other.area()
    
    def __ne__(self, other):
        """
        Not equal comparison operator.

        Args:
            other: The other Square object.

        Returns:
            bool: True if self's area is not equal to other's area, False otherwise.
        """
        return self.area() != other.area()
    
    def __gt__(self, other):
        """
        Greater than comparison operator.

        Args:
            other: The other Square object.

        Returns:
            bool: True if self's area is greater than other's area, False otherwise.
        """
        return self.area() > other.area()
    
    def __ge__(self, other):
        """
        Greater than or equal comparison operator.

        Args:
            other: The other Square object.

        Returns:
            bool: True if self's area is greater than or equal to other's area, False otherwise.
        """
        return self.area() >= other.area()
