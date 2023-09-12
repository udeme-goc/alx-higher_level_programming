#!/usr/bin/python3
"""
This module provides a function to check if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The specified class.

    Returns:
        bool: True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) == a_class
