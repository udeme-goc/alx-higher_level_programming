#!/usr/bin/python3

# Define the function safe_print_list_integers
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x integers from a given list.
    """
    # Initialize a counter variable
    i = 0
    
    # Iterate through the range from 0 to x-1
    for j in range(x):
        try:
            # Try to print the j-th element of my_list as an integer
            print("{:d}".format(my_list[j]), end="")
            
            # Increment the counter
            i += 1
        except (ValueError, TypeError):
            # If ValueError or TypeError occurs (non-integer element), continue to the next iteration
            continue
    
    # Print a newline character after printing the integers
    print()
    
    # Return the count of successfully printed integers
    return i

