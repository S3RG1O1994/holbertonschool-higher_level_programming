#!/usr/bin/python3
"""Class square create one object with an size define

Raises:
    TypeError: [When size is different of int]
    ValueError: [When size is less that Zero]
    TypeError: [When value is different of int]
    ValueError: [When value is less that Zero]

Returns:
    [Int] -- [attribute private size to public and total area of an square]
"""


class Square:
    """class constructor"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """class getter"""
    @property
    def size(self):
        return self.__size

    """class setter"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """class getter"""
    @property
    def position(self):
        return self.__position

    """class setter"""
    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[1]) != int or type(value[0]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[1] < 0 or value[0] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = value

    """class for obtain total area of the square"""
    def area(self):
        return self.__size * self.__size

    """method for print object based in his size with space """
    def my_print(self):
        if self.size == 0:
            print()
        else:
            if self.position[1] != 0:
                print('\n' * self.position[1], end="")
            for sqr in range(self.size):
                print(' ' * self.position[0], end="")
                print('#' * self.size)
