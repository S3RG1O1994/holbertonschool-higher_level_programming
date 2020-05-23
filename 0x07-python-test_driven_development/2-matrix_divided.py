#!/usr/bin/python3
""" matrix_divided is an function for create new matrix with the division
    by value in div in each of the matrix
"""


def matrix_divided(matrix, div):
    """[matrix_divided]

    Arguments:
        matrix {[list of list]} -- [matrix-2D of integer]
        div {[int]} -- [Number for division each item in the matrix]

    Raises:
        TypeError: [matrix must be a matrix (list of lists) of integers/floats]
        TypeError: [Each row of the matrix must have the same size]
        TypeError: [div must be a number]
        ZeroDivisionError: [division by zero]

    Returns:
        [list] -- [New_matrix with result operation]
    """
    error = 'matrix must be a matrix (list of lists) of integers/floats'
    if (not matrix or type(matrix) is not list
            or matrix is []
            or not all([type(row) is list for row in matrix])
            or not all([[type(el) is int for el in row] for row in matrix])
            or not all([[type(el) is float for el in row] for row in matrix])):
        raise TypeError(error)
    if len(set([len(rows) for rows in matrix])) != 1:
        raise TypeError('Each row of the matrix must have the same size')
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = [[round(num / div, 2) for num in col] for col in matrix]
    return new_matrix
