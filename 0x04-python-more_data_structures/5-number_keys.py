#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    Return the number of keys in a dictionary.

    Args:
    a_dictionary (dict): The dictionary.

    Returns:
    int: Number of keys in dictionary.
    """
    # Use the len() function to calaculate the number of keys
    num_keys = len(a_dictionary)

    return num_keys

# Test the function
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
