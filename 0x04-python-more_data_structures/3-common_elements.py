#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Return a set of common elements between two sets.

    Args:
    set_1 (set): The first set.
    set_2 (set): The second set.

    Returns:
    set: Set containing common elements.
    """

    # Initialize an empty set to store common elements
    common_set = set()

    # Iterate through elements in set_1
    for element in set_1:
        # Check if the elements in set_2
        if element in set_2:
            # Add the element to the common_set
            common_set.add(element)

    return common_set
