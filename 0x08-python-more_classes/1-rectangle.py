#!/usr/bin/python3
"""class for create an object called rectangle, with an width and height gives.

Raises:
    TypeError: [width must be an integer]
    ValueError: [width must be >= 0]
    TypeError: [height must be an integer]
    ValueError: [height must be >= 0]

Returns:
    [attribute] -- [the attribute private for change his value]
"""


class Rectangle:
    """Class constructor"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """class getter"""
    @property
    def width(self):
        return self.__width

    """Class setter"""
    @width.setter
    def width(self, value):
        if value is int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    """class getter"""
    @property
    def height(self):
        return self.__height

    """Class setter"""
    @height.setter
    def height(self, value):
        if value is int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be >= 0')
        self.__height = value
