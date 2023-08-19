#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Update or add a key-value pair in a dictionary.

    Args:
    a_dictionary (dict): The dictionary.
    key (str): The key to update or add.
    value: The value to update or add.
    
    Returns:
    dict: The updated dictionary.
    """
    # Update the value if the key exists, or add the key-value pair
    a_dictionary[key] = value
    
    return a_dictionary
