#!/usr/bin/python3

def safe_print_integer(value):
    """
    Safely prints an integer value.

    Args:
        value: The value to be printed.

    Returns:
        bool: True if value is an integer and is successfully printed, False otherwise.
    """
    try:
        print("{:d}".format(value))  # Try to print the integer value
    except (ValueError, TypeError):
        # If a ValueError or TypeError occurs (value is not an integer),
        # return False
        return False
    else:
        # If no exception occurred and the value was successfully printed,
        # return True
        return True

