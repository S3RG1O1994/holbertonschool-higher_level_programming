#!/usr/bin/python3
"""[class Rectangle is for create an object]
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """[class Rectangle]

    Arguments:
        BaseGeometry {[class]} -- [super class]
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
