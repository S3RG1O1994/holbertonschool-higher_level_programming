#!/usr/bin/python3
"""class Square create one object instance an size for the square
    size is have validate(type data/ Value data)

Raises:
    TypeError: [When size is not int]
    ValueError: [When size is less that Zero]

Returns:
        [int] -- [Total Area the object create with an size]
"""


class Square:
    """class constructor"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """ method for obtain area the self object"""
    def area(self, __size=0):
        return self.__size * self.__size
