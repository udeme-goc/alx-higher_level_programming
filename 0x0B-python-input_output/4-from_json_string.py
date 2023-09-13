#!/usr/bin/python3
"""
This script defines a function from_json_string that converts a JSON string
to its corresponding Python object.

Usage: ./4-from_json_string.py
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON string to its corresponding Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        obj: The Python object corresponding to the JSON string.
    """
    # Using json.loads to convert the JSON string to a Python object
    return json.loads(my_str)


if __name__ == "__main__":
    # Example usage with a JSON string representing a list
    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
    print(type(my_list))

    # Example usage with a JSON string representing a dictionary
    s_my_dict = """
    {
        "is_active": true,
        "info": {
            "age": 36,
            "average": 3.14
        },
        "id": 12,
        "name": "John",
        "places": ["San Francisco", "Tokyo"]
    }
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))

    # Example usage with invalid JSON string (demonstrates non-parsable case)
    try:
        s_invalid_json = """
        {
            is_active: true,
            12
        }
        """
        my_obj = from_json_string(s_invalid_json)
        print(my_obj)
        print(type(my_obj))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
