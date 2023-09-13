#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then saves them to a file
as a JSON representation.

Usage: ./7-add_item.py [arg1] [arg2] ...

Arguments:
    arg1, arg2, ... : Items to be added to the list.

Example:
    ./7-add_item.py Best School
"""

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Define the file name
filename = "add_item.json"

# Check if the file exists
if path.exists(filename):
    # Load existing list from the file
    my_list = load_from_json_file(filename)
else:
    # Create a new list if the file doesn't exist
    my_list = []

# Add arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
