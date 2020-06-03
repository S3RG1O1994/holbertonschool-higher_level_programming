#!/usr/bin/python3
"""[class bassGeometry contain base for anyfigure geometric]

Raises:
    Exception: [area() is not implemented]
    TypeError: [<name> must be an integer]
    ValueError: [<name> must be greater than 0]
"""


class BaseGeometry:
    """[function for find area]
    """

    def area(self):
        raise Exception('area() is not implemented')

    """[function for validate type or quantity of the value]
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError('<name> must be greater than 0')
        self.name = name

    """[class Rectangle create an object with characteristics of an rectangle]
    """


class Rectangle(BaseGeometry):
    """[Sub class based in BaseGeometry]

    Arguments:
        BaseGeometry {[class]} -- [super class with data necessary]
    """

    """[Method constructor]
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """[edit str method for this method]
    """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    """[method for find area of an rectangle]
    """
    def area(self):
        return self.__width * self.__height
