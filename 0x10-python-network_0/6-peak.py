#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int or None: Peak element in the list or None if the list is empty.
    """

    # Check if the list is empty
    if not list_of_integers:
        return None

    # Initialize low and high pointers
    low = 0
    high = len(list_of_integers) - 1

    # Perform binary search to find the peak
    while low < high:
        mid = (low + high) // 2

        # Compare the middle element with its neighbour
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    # Return the peak element
    return list_of_integers[low]

# Test the function
if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))   # Output: 6
    print(find_peak([4, 2, 1, 2, 3, 1]))   # Output: 4
    print(find_peak([2, 2, 2]))   # Output: 2
    print(find_peak([]))   # Output: None
    print(find_peak([-2, -4, 2, 1]))   # Output: 2
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))   # Output: 4
