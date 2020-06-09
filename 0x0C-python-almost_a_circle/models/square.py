#!/usr/bin/python3
"""[class Square, for create an object square]

Returns:
    [Object]: [instance]
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """[class constructor]
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """[change data size]
        """
        return self.width

    @size.setter
    def size(self, value):
        """[Setting data]
        """
        self.width = value
        self.height = value

    def __str__(self):
        """[change str for print]
        """
        string = '[Square] ({}) {}/{} - {}'
        return string.format(self.id, self.x, self.y, self.size)

    def to_dictionary(self):
        """[Create an dictionary]
        """
        atr = {}
        atr["id"] = self.id
        atr["size"] = self.size
        atr["x"] = self.x
        atr["y"] = self.y
        return atr

    def update(self, *args, **kwargs):
        """[Update data]
        """
        atr = ['id', 'size', 'x', 'y']
        for atr, arg in zip(atr, args):
            setattr(self, atr, arg)
        for keys, value in kwargs.items():
            setattr(self, keys, value)
