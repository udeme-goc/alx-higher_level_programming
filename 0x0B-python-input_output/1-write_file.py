#!/usr/bin/python3
"""
This function writes a string to a text file (UTF8) and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written.
    """
    # Open the file in write mode with UTF-8 encoding
    with open(filename, 'w', encoding='utf-8') as file:
        # Write the text to the file and return number of characters written
        return file.write(text)
