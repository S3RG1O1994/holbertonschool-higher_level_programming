#!/usr/bin/python3
"""Class square create one object with an size define

Raises:
    TypeError: [When size is different of int]
    ValueError: [When size is less that Zero]
    TypeError: [When value is different of int]
    ValueError: [When value is less that Zero]

Returns:
    [Int] -- [attribute private size to public and total area of an square]
"""


class Square:
    """class constructor"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """class getter"""
    @property
    def size(self):
        return self.__size

    """class setter"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """class for obtain total area of the square"""
    def area(self, __size=0):
        return self.__size * self.__size

    """method for print object based in his size"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for sqr in range(self.__size):
                for icon in range(self.__size):
                    print('#', end="")
                print()
