#!/usr/bin/python3
"""Define instant of one object square with private attribute
    Size is have validate(type data/ Value data)

Raises:
    TypeError: [When type of data within size is not int]
    ValueError: [When size is less that Zero]
"""


class Square:
    """class constructor"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
