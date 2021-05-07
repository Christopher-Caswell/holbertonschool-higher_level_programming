#!/usr/bin/python3
"""
Return a division of matrix[[]] by div
Edge cases made against the output:
div must be an integer
matrix must be a list of lists
lists in matrix must be the same length
"""


def matrix_divided(matrix, div):
    """Let's geographicize this matrix"""
    item_comp = matrix[0]
    """Necessary to volumize later"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
            raise TypeError("matrix must be a matrix (list of "
                            "lists) of integers/floats")
    for items in matrix:
        if not isinstance(items, list):
            raise TypeError("matrix must be a matrix (list of "
                            "lists) of integers/floats")
        for x in items:
            if type(x) is not int:
                raise TypeError("matrix must be a matrix (list of "
                                "lists) of integers/floats")
    for item in matrix:
        if len(item) is not len(item_comp):
            raise TypeError("Each row of the matrix "
                            "must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new = (list(map(lambda x: list(map(
           lambda y: round(y / div, 2), x)), matrix)))
    return new
