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
        """[Modification str for print]
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    def validate(self, name, value):
        """[method validate data]
        """
        dimensions = ['width', 'height']
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and name in dimensions:
            raise ValueError('{} must be > 0'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    @property
    def width(self):
        """[Change attribute width]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """[Change attribute width]
        """
        self.validate('width', value)
        self.__width = value

    @property
    def height(self):
        """[Change attribute height]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """[Change attribute height]
        """
        self.validate('height', value)
        self.__height = value

    @property
    def x(self):
        """[Change attribute x]
        """
        return self.__x

    @x.setter
    def x(self, value):
        """[Change attribute x]
        """
        self.validate('x', value)
        self.__x = value

    @property
    def y(self):
        """[Change attribute y]
        """
        return self.__y

    @y.setter
    def y(self, value):
        """[Change attribute y]
        """
        self.validate('y', value)
        self.__y = value

    def area(self):
        """[Method for find area of an instance]
        """
        return self.__width * self.__height

    def display(self):
        """[Function print form of an instance]
        """
        figure = ('\n' * self.__y)
        for col in range(self.__height):
            print(' ' * self.__x, end="")
            print('#', * self.__width) + '\n'
        print(figure, end="")

    def update(self, *args, **kwargs):
        """[Function for update data]
        """
        atr = ["id", "width", "height", "x", "y"]
        for atr, arg in zip(atr, args):
            setattr(self, atr, arg)
        for keys, value in kwargs.items():
            setattr(self, keys, value)

    def to_dictionary(self):
        """[Method for create an dictionary]
        """
        atr = {}
        atr["id"] = self.id
        atr["width"] = self.width
        atr["height"] = self.height
        atr["x"] = self.x
        atr["y"] = self.y
        return atr
