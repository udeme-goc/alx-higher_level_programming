#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Calculate the weighted average of integers based on the given list of tuples.

    Args:
    my_list (list): List of tuples containing integers and their corresponding weights.

    Returns:
    float: The weighted average.
    """
    # If the list is empty, return 0
    if not my_list:
        return 0
    
    # Initialize variables to calculate the numerator and denominator of the weighted average
    numerator = 0
    denominator = 0
    
    # Iterate through the tuples in the list
    for score, weight in my_list:
        numerator += score * weight
        denominator += weight
    
    # Calculate and return the weighted average
    weighted_average = numerator / denominator
    return weighted_average
