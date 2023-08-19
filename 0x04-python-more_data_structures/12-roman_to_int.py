#!/bin/usr/python3

def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.

    Args:
    roman_string (str): The Roman numeral string.

    Returns:
    int: The integer equivalent of the Roman numeral.
    """
    # Define a dictionary for Roman numeral symbols and their values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    # Initialize the result
    result = 0
    
    # Initialize a variable to keep track of the previous value
    prev_value = 0
    
    # Iterate through the characters in the reversed Roman numeral string
    for char in reversed(roman_string):
        # Get the value of the current character from the dictionary
        current_value = roman_values[char]
        
        # If the current value is smaller than the previous value,
        # subtract it from the result; otherwise, add it to the result
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        
        # Update the previous value
        prev_value = current_value
    
    return result
