#!/usr/bin/python3

def magic_calculation(a, b):
    """
    Performs a series of calculations based on input values a and b.

    Args:
        a: First input value.
        b: Second input value.

    Returns:
        float: The result of the calculations.
    """
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')

            result += a ** b / i
        except:
            result = b + a
            break

    return result
