#!/usr/bin/python3


class MyList(list):
    """
    Class representing a custom list that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list, sorted in ascending order.
        """
        print(sorted(self))
