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
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
