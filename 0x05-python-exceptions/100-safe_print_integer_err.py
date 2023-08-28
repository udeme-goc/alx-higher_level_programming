#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    Safely prints an integer and handles exceptions.
    
    Args:
        value: The value to be printed (can be of any type).
        
    Returns:
        bool: True if value is an integer and has been printed, False otherwise.
    """
    try:
        print("{:d}".format(value))  # Try to format and print the value as an integer
        return True  # Return True if successful
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)  # Print the exception to stderr
        return False  # Return False if the value cannot be formatted as an integer

