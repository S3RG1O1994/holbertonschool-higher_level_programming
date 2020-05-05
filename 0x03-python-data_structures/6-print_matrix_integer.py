#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in matrix[i]:
            if j != len(matrix[i]) and i == 0:
                print('{:d}'.format(j), end="")
            elif i > 0 and j != len(matrix[i]) * 2:
                print('{:d}'.format(j), end="")
            else:
                print('{:d}'.format(j))
    print()
