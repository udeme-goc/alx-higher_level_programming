#!/usr/bin/python3
"""
This script defines a function load_from_json_file that creates an object from
a JSON file.

Usage: ./6-load_from_json_file.py
"""

import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        obj: The object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == "__main__":
    # Example usage with a JSON file representing a list
    filename_list = "my_list.json"
    my_list = load_from_json_file(filename_list)
    print(my_list)
    print(type(my_list))

    # Example usage with a JSON file representing a dictionary
    filename_dict = "my_dict.json"
    my_dict = load_from_json_file(filename_dict)
    print(my_dict)
    print(type(my_dict))

    # Example usage with a non-existent file (to demonstrate FileNotFoundError)
    try:
        filename_nonexistent = "my_nonexistent.json"
        my_obj = load_from_json_file(filename_nonexistent)
        print(my_obj)
        print(type(my_obj))
    except FileNotFoundError as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    # Example usage with an invalid JSON file (to demonstrate JSONDecodeError)
    try:
        filename_invalid_json = "my_fake.json"
        my_obj = load_from_json_file(filename_invalid_json)
        print(my_obj)
        print(type(my_obj))
    except json.decoder.JSONDecodeError as e:
        print("[{}] {}".format(e.__class__.__name__, e))
