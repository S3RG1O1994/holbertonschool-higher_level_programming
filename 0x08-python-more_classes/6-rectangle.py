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
    number_of_instances = 0

    """class constructor"""
    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    """class getter"""
    @property
    def width(self):
        return self.__width

    """Class setter"""
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    """class getter"""
    @property
    def height(self):
        return self.__height

    """Class setter"""
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    """method for print area the object instances"""
    def area(self):
        return self.width * self.height

    """method for print perimeter the object instances"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    """Function print string"""
    def __str__(self):
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for col in range(self.height):
            for str in range(self.width):
                string += '#'
            if col != self.height - 1:
                string += '\n'
        return string

    """Method for print string of the object"""
    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)

    """method destructor"""
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
