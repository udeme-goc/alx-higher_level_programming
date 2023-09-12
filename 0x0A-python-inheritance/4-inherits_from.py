#!/usr/bin/python3
"""
Function checks if object is instance of class inheriting from specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is instance of a class inheriting from specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The specified class.

    Returns:
        bool: True if obj is instance of a subclass of a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
