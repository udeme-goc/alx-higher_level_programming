#!/usr/bin/python3
"""
This module defines a function add_attribute to add attributes to objects.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to which the attribute is to be added.
        name (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
