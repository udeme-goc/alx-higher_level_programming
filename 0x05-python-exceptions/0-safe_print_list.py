#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safely prints elements from a list up to a specified limit.

    Args:
        my_list (list, optional): The list containing elements to print.
        x (int, optional): The maximum number of elements to print.

    Returns:
        int: The actual number of elements printed.

    """
    n = 0  # Initialize a counter to track the number of printed elements

    # Loop through the range of x (the specified limit)
    for m in range(x):
        try:
            print(my_list[m], end="")  # Print the element without a new line
            n += 1  # Increment the counter for each printed element
        except IndexError:
            # If an IndexError occurs (element not present in the list),
            # break out of the loop
            break

    print()  # Print a new line after all elements are printed
    return n  # Return the actual number of elements printed
