#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Return a set of elements present in only one set.

    Args:
    set_1 (set): The first set.
    set_2 (set): The second set.

    Returns:
    set: Set containing elements present in only one set.
    """

    # Initialize an empty set to store elements present in only one set
    unique_set = set()

    # Iterate through elements in set_1
    for element in set_1:
        # Check if the element is not in set_2
        If element not in set_2:
            # Add the element to the unique_set
            unique_set.add(element)

    # Iterate through elements in set_2
    for element in set_2:
        # Check if the element is not in set_1
        if element not in set_1:
            # Add the element to the unique_set
            unique_set.add(element)

    return unique_set
