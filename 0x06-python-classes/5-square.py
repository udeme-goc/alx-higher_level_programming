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
            value (int): The new size value.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        Prints the square pattern using '#'.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
