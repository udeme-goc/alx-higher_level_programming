#!/usr/bin/python3
"""
This module provides a function for inserting a line of text after each line
containing a specific string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts line of text to a file, after each line containing specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str):
                The string to append after lines containing `search_string`.

    Returns:
        None

    Note:
        This function assumes that the file exists and is readable/writable.

    Example:
        Consider a file 'example.txt' with the following content:

            Line 1: Hello
            Line 2: Python is fun!
            Line 3: Goodbye

        Calling `append_after('example.txt', 'Python', 'C is fun!\\n')`
        would result in:

            Line 1: Hello
            Line 2: Python is fun!
            C is fun!
            Line 3: Goodbye
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + "\n")
        file.truncate()