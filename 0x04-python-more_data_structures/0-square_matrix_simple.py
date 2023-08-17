#!/usr/bin/python3

def square_matric_simple(matrix=[]):
    """
    Compute the square value of all integers in a matrix.

    Args:
    matrix (lists of lists): The 2-dimensional array.

    Returns:
    List of lists: New matrix with squared values.
    """
    # Create an empty matrix to store squared values
    new_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create an empty row for the new_matrix
        new_row = []

        # Iterate through each element in the current row
        for element in row:
            # Compute the square of the element and append to the new_row
            new_row.append(element ** 2)

        # Append the new_row to the new_matrix
        new_matrix.append(new_row)

    return new_matrix
