#!/usr/bin/python3
"""
This script defines a function append_write that appends a string to the end
of a text file and returns the number of characters added.

Usage: ./2-append_write.py [filename] [text]
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the
    number of characters added.

    Args:
        filename (str): The name of the file to be appended.
        text (str): The text to be appended.

    Returns:
        int: The number of characters added.

    Raises:
        IOError: If an error occurs while appending to the file.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except IOError as e:
        print(f"Error: {e}")
        return 0


if __name__ == "__main__":
    # Example usage
    filename = "file_append.txt"
    text_to_append = "This School is so cool!\n"

    nb_characters_added = append_write(filename, text_to_append)
    print(nb_characters_added)
