#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Return a new list with values multiplied by a number using map.

    Args:
    my_list (list): The list of integers.
    number (int): The number to multiply by.

    Returns:
    list: New list with values multiplied by the number.
    """
    return list(map(lambda x: x * number, my_list))
i
