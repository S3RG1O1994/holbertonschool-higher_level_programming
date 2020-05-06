#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j < len(matrix):
                print('{:d}'.format(j), end="")
            elif j < len(matrix) * 2:
                print('{:d}'.format(j), end="")
            else:
                print('{:d}'.format(j), end="")
        print()
