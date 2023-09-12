#!/usr/bin/python3
"""
Module defines MyInt class extending int with inverted == and != operators.
"""


class MyInt(int):
    """
    MyInt class extends int and inverts == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)
