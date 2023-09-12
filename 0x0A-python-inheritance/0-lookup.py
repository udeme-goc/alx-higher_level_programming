#!/usr/bin/python3
"""
Provides a function to retrieve the attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object to retrieve attributes and methods from.

    Returns:
        list: A list containing the names of attributes and methods.

    """
    return dir(obj)
