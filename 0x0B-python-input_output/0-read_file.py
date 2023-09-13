#!/usr/bin/python3
"""
0-read_file.py - Read and print the content of a text file.

This script defines a function read_file that reads a text file and prints its
content to the standard output.

Usage: ./0-read_file.py [filename]
"""

def read_file(filename=""):
    """
    Read and print the content of a text file.

    Args:
        filename (str): The name of the file to be read. Default is an empty string.

    Returns:
        None
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    # If the script is run directly, read the file specified in the command line
    read_file()
