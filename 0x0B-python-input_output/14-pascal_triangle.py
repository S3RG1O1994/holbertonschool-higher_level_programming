#!/usr/bin/python3
"""[Function create an pascal triangle of an number]
"""


def pascal_triangle(n):
    pascal = list()
    if n == 0:
        return pascal
    else:
        pascal.append([1])

        for num in range(1, n):
            ant = pascal[-1]
            sig = [1]
            for num in range(len(ant) - 1):
                sig.append(ant[num] + ant[num + 1])
            sig += [1]
            pascal.append(sig)
        return pascal
