#!/usr/bin/python3
"""[Subclass Rectangle for bulding an rectangle]

Returns:
    [int]: [privatization of attributes]
"""

from models.base import Base


class Rectangle(Base):
    """[Class constructor]

    Args:
        Base ([Superclass]): [count number instances]
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        string = '[Rectangle] ({}) {}/{} - {}/{}'
        return string.format(self.id, self.__x, self.__y, self.__width, self.__height)

    """[method validate data]
    """
    def validate(self, name, value):
        dimensions = ['width', 'height']
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and name in dimensions:
            raise ValueError('{} must be > 0'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    """[Change attribute width]
    """
    @property
    def width(self):
        return self.__width

    """[Change attribute width]
    """
    @width.setter
    def width(self, value):
        self.validate('width', value)
        self.__width = value

    """[Change attribute height]
    """
    @property
    def height(self):
        return self.__height

    """[Change attribute height]
    """
    @height.setter
    def height(self, value):
        self.validate('height', value)
        self.__height = value

    """[Change attribute x]
    """
    @property
    def x(self):
        return self.__x

    """[Change attribute x]
    """
    @x.setter
    def x(self, value):
        self.validate('x', value)
        self.__x = value

    """[Change attribute y]
    """
    @property
    def y(self):
        return self.__y

    """[Change attribute y]
    """
    @y.setter
    def y(self, value):
        self.validate('y', value)
        self.__y = value

    """[Method for find area of an instance]
    """
    def area(self):
        return self.__width * self.__height

    def display(self):
        for col in range(self.__height):
            print(' ' * self.__x, end="")
            for item in range(self.width):
                print('#', end="")
            print()

    def update(self, *args):
        new_list = [items for items in args]
        if len(new_list) == 1:
            self.id = new_list[0]
        if len(new_list) == 2:
            self.id = new_list[0]
            self.__width = new_list[1]
        if len(new_list) == 3:
            self.id = new_list[0]
            self.__width = new_list[1]
            self.__height = new_list[2]
        if len(new_list) == 4:
            self.id = new_list[0]
            self.__width = new_list[1]
            self.__height = new_list[2]
            self.__x = new_list[3]
        if len(new_list) == 5:
            self.id = new_list[0]
            self.__width = new_list[1]
            self.__height = new_list[2]
            self.__x = new_list[3]
            self.__y = new_list[4]
