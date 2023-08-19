#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Return a new dictionary with values multiplied by 2.

    Args:
    a_dictionary (dict): The dictionary with integer values.

    Returns:
    dict: New dictionary with values multiplied by 2.
    """
    # Create a new dictionary to store the multiplied values
    new_dict = {}
    
    # Iterate through the dictionary items
    for key, value in a_dictionary.items():
        # Multiply the value by 2 and store it in the new dictionary
        new_dict[key] = value * 2
    
    return new_dict
