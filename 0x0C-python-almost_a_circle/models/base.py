#!/usr/bin/python3
"""Defines the Base class."""


class Base:
    """Represents the base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance.

        Args:
            id (int): The identifier. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
