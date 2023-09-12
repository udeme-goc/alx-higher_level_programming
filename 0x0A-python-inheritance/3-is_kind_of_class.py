#!/usr/bin/python3
"""
Function checks if object is instance of or inherits from specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherits from, a specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is instance or inherits from a_class, else False.
    """
    return isinstance(obj, a_class)
