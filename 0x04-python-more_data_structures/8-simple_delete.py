imple_delete(a_dictionary, key=""):
    """
    Delete a key from a dictionary.

    Args:
    a_dictionary (dict): The dictionary.
    key (str): The key to delete.

    Returns:
    dict: The updated dictionary.
    """
    # Check if the key exists in the dictionary before deleting
    if key in a_dictionary:
        del a_dictionary[key]
    
    return a_dictionary
