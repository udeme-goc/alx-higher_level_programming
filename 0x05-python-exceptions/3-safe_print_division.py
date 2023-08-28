#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides two integers and prints the result.
    
    Args:
        a (int): The numerator.
        b (int): The denominator.
        
    Returns:
        float or None: The result of the division, or None if division by zero occurs.
    """
    result = None  # Initialize the result variable
    
    try:
        result = a / b  # Perform the division
    except ZeroDivisionError:
        pass  # Ignore ZeroDivisionError, which occurs if b is 0
    finally:
        print("Inside result: {}".format(result))  # Print the result in the finally block
        
    return result  # Return the result of the division or None if division by zero
