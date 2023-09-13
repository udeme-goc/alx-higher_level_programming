#!/usr/bin/python3
"""
Pascal's Triangle Module
"""


def pascal_triangle(n):
    """
    Generates a Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows in the Pascal's Triangle.

    Returns:
        list of list of int:
                A list containing lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)
        row.append(1)
        triangle.append(row)

    return triangle

# Step by step implementation comments:

# 1. The function `pascal_triangle` takes an integer `n` as input,
#        representing the number of rows in the Pascal's Triangle.
# 2. It first checks if `n` is less than or equal to zero.
#        If so, it returns an empty list, as there are no rows to generate.
# 3. Initialize `triangle` as a list containing a single list
#        with the element 1. This represents first row of Pascal's Triangle.
# 4. Loop from the second row (index 1) up to the `n`-th row.
# 5. For each row, initialize `row` as a list with the first element set to 1
#        (the leftmost element is always 1).
# 6. Loop from the second element (index 1) up to the second-to-last element
#        of the row.
# 7. For each element in the row (except the first and last),
#        calculate it by summing the corresponding elements from previous row.
# 8. Append the calculated element to the `row`.
# 9. After the inner loop, append last element of the row, which is always 1.
# 10. Append the generated `row` to the `triangle`.
# 11. Repeat steps 4-10 until all `n` rows are generated.
# 12. Finally, return the generated Pascal's Triangle.


# Example Usage:
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)
