#!/usr/bin/python3
"""class Rectangle create an object with width and height gives
    so i have methods for print area or parameter.

Raises:
    TypeError: [width must be an integer]
    ValueError: [width must be >= 0]
    TypeError: [height must be an integer]
    ValueError: [height must be >= 0]

Returns:
    [attribute] -- [Attribute private change to public]
"""


class Rectangle:
    """class constructor"""
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

    """method for print area the object instances"""
    def area(self, __width=0, __height=0):
        return self.__width * self.__height

    """method for print perimeter the object instances"""
    def perimeter(self, __width=0, __height=0):
        return (self.__width * 2) + (self.__height * 2)

    """Function print string"""
    def __str__(self):
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for col in range(self.height):
            for str in range(self.width):
                string += '#'
            string += '\n'
        return string