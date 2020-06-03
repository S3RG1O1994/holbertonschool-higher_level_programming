#!/usr/bin/python3
"""[Import super class Rectangle]

Returns:
    [string] -- [Details for find the area in an square]
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """[class for create objects as an square]

    Arguments:
        Rectangle {[SuperClass]} -- [class that inherit items necessary]
    """

    def __init__(self, size):
        """method constructor"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """edit str method"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
