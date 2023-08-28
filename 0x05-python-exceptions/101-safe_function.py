#!/usr/bin/python3

def safe_function(fct, *args):
    """
    Executes a function safely and handles exceptions.
    
    Args:
        fct (function): The function to be executed.
        *args: Variable number of arguments to be passed to the function.
        
    Returns:
        The result of the function, or None if an exception occurs.
    """
    try:
        result = fct(*args)  # Call the provided function with the arguments
        return result  # Return the result if successful
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)  # Print the exception to stderr
        return None  # Return None if an exception occurs

