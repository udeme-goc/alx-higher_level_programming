#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    Safely prints an integer value and handles exceptions.

    Args:
        value: The value to be printed.

    Returns:
        bool: True if the value is an integer and is successfully printed, False otherwise.
    """
    try:
        print("{:d}".format(value))  # Try to print the integer value
    except (ValueError, TypeError) as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return False
    else:
        return True
