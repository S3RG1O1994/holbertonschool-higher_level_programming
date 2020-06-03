#!/usr/bin/python3
"""[class bassGeometry contain base for anyfigure geometric]
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """[Sub class based in BaseGeometry]

    Arguments:
        BaseGeometry {[class]} -- [super class with data necessary]
    """

    """[Method constructor]
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """[edit str method for this method]
    """
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    """[method for find area of an rectangle]
    """
    def area(self):
        return self.__width * self.__height
