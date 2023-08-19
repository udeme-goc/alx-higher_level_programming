#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Return the key with the biggest integer value in a dictionary.

    Args:
    a_dictionary (dict): The dictionary with integer values.

    Returns:
    str: The key with the biggest integer value.
    """
    # Initialize variables to keep track of the best score and key
    best_key = None
    best_score = float('-inf')  # Negative infinity
    
    # Iterate through the dictionary items
    for key, value in a_dictionary.items():
        # Compare the current value with the best score
        if value > best_score:
            best_score = value
            best_key = key
    
    return best_key
