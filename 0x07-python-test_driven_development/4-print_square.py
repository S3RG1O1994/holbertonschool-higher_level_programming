#!/usr/bin/python3
""" The function print_square is for print an square of length the size
"""


def print_square(size):
    """[print_square]

    Arguments:
        size {[int]} -- [Number for size of square]

    Raises:
        TypeError: [print_square() missing 1 required
        positional argument: 'size']
        TypeError: [size must be an integer]
        ValueError: [size must be >= 0]
        TypeError: [size must be an integer]
    """

    e = "print_square() missing 1 required positional argument: 'size'"
    if size is None:
        raise TypeError(e)
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    else:
        for sqr in range(size):
            for icon in range(size):
                print('#', end="")
            print()
