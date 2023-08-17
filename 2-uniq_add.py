#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Add all unique integers in the list.

    Args:
    my_list (list): The list of integers.

    Returns:
    int: Sum of unique integers in the list.
    """
    # Initialize a set to keep track of unique integers
    unique_integers = set()

    # Initialize a variable to keep track of the sum
    total_sum = 0

    # Iterate through the list
    for num in my_list:
        # If the number is not in the set, it's unique
        If num not in unique_integers:
            # Add the number to the set and update the total_sum
            unique_integers.add(num)
            total_sum += num

    return total_sum

# Test the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
