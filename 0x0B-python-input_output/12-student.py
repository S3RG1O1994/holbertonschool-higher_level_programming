#!/usr/bin/python3
"""[class student create an obj students]

Returns:
    [dict] -- [dictionary]
"""


class Student:
    """[Class Constructor]
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """[Class create JSON]
    """

    def to_json(self, attrs=None):
        """method for return dictionary"""

        if isinstance(attrs, list) and all(isinstance(attr, str)
                                        for attr in attrs):
            rta = {}
            for i in attrs:
                if i in self.__dict__:
                    rta[i] = self.__dict__[i]
            return rta
        return self.__dict__
