#!/usr/bin/python3
"""
This script defines a function save_to_json_file that saves an object to a
JSON file using a JSON representation.

Usage: ./5-save_to_json_file.py
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to save to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)


if __name__ == "__main__":
    # Example usage with a list
    filename_list = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename_list)

    # Example usage with a dictionary
    filename_dict = "my_dict.json"
    my_dict = {
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename_dict)

    # Example usage with invalid object (demonstrates non-serializable case)
    try:
        filename_set = "my_set.json"
        my_set = {132, 3}
        save_to_json_file(my_set, filename_set)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
