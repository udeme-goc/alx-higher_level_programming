#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Safely prints the first x integers of a list.
    
    Args:
        my_list (list): The input list containing elements of any type.
        x (int): The number of elements to access and print.
        
    Returns:
        int: The real number of integers printed.
    """
    integers_printed = 0  # Initialize a counter for the integers printed
    
    try:
        for i in range(x):  # Loop through the first x elements
            if isinstance(my_list[i], int):  # Check if the element is an integer
                print("{:d}".format(my_list[i]), end='')  # Print the integer without a new line
                integers_printed += 1  # Increment the counter
        print()  # Print a new line after printing the integers
    except IndexError:
        pass  # Ignore IndexError, which occurs if x is larger than the list length
    
    return integers_printed  # Return the number of integers printed

#
