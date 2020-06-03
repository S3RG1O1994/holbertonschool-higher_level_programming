#!/usr/bin/python3
"""[Create subclass of Rectangle]
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """[class for create objects as an square]

    Arguments:
        Rectangle {[SuperClass]} -- [class that inherit items necessary]
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
