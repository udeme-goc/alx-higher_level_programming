#!/usr/bin/python3

class Square:
    """
    This is the Square class documentation.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position
    
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
    
    @property
    def position(self):
        """
        Retrieves the value of the position attribute.
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """
        Sets the value of the position attribute.

        Args:
            value (tuple): The new position value.
        """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
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
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
    
    def __str__(self):
        """
        Generates a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        result = []
        if self.__size == 0:
            result.append('')
        else:
            for _ in range(self.__position[1]):
                result.append('')
            for _ in range(self.__size):
                result.append(" " * self.__position[0] + "#" * self.__size)
        return '\n'.join(result)
