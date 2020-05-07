#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = [[num ** 2 for num in col] for col in matrix]
    return copy
