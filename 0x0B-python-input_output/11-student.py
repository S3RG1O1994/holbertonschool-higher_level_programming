#!/usr/bin/python3
"""[Class for create obj student]

Returns:
    [dict] -- [dictionary]
"""


class Student:
    """[method constructor]
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """[method for create JSON]
    """
    def to_json(self):
        return self.__dict__.copy()
