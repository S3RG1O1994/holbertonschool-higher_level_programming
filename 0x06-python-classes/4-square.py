#!/usr/bin/python3
"""Class square create one object with an size
    size have verifications(type-data / value-data)

Raises:
    TypeError: [When size is not int]
    ValueError: [When is less that Zero]
    TypeError: [When value is not int]
    ValueError: [When value less that Zero]

Returns:
    [int] -- [size how public attribute and total area the object]
"""


class Square:
    """class constructor"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """size getter"""
    @property
    def size(self):
        return self.__size

    """size setter"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """method for obtain area the object"""
    def area(self, __size=0):
        return self.__size * self.__size
