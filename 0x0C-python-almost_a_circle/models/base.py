#!/usr/bin/python3
"""[Class Base for create elements and i can have an counter of id]
"""


class Base:
    __nb_objects = 0

    """[Class constructor]
    """
    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
