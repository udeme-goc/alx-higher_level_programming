#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    Compute the square value of all integers in a matrix using map.

    Args:
    matrix (list): 2D list (matrix) of integers.

    Returns:
    list: New matrix with squared values.
    """
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
