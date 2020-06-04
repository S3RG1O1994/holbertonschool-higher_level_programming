#!/usr/bin/python3
"""[Class student create an obj]

Returns:
    [dict] -- [dictionary]
"""


class Student:
    """[class constructor]
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """[method create JSON]
    """
    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                            for attr in attrs):
            rta = {}
            for i in attrs:
                if i in self.__dict__:
                    rta[i] = self.__dict__[i]
            return rta
        return self.__dict__

    """[Method create dict]
    """
    def reload_from_json(self, json):
        for atr in json:
            self.__dict__[atr] = json[atr]
