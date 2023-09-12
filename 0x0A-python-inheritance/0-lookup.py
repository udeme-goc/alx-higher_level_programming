#!/usr/bin/python3


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object to retrieve attributes and methods from.

    Returns:
        list: A list containing the names of attributes and methods.

    """
    return dir(obj)
