#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Delete keys with a specific value in a dictionary.

    Args:
    a_dictionary (dict): The dictionary to modify.
    value: The value to search for and delete.

    Returns:
    dict: The modified dictionary.
    """
    # Create a list of keys to delete
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    
    # Delete the keys from the dictionary
    for key in keys_to_delete:
        del a_dictionary[key]
    
    return a_dictionary
