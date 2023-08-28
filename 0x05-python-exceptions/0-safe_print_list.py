#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safely prints x elements of a list.
    
    Args:
        my_list (list): The input list containing elements of any type.
        x (int): The number of elements to print.
        
    Returns:
        int: The real number of elements printed.
    """
    elements_printed = 0  # Initialize a counter for the elements printed
    
    try:
        for i in range(x):  # Loop through the first x elements
            print(my_list[i], end='')  # Print the element without a new line
            elements_printed += 1  # Increment the counter
    except IndexError:
        pass  # Ignore IndexError, which occurs if x is larger than the list length
    
    print()  # Print a new line after printing the elements
    return elements_printed  # Return the number of elements printed
