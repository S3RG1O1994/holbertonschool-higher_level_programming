#!/usr/bin/python3
"""[Class Base for create elements and i can have an counter of id]
"""

import json
import os


class Base:
    """Class Base"""
    __nb_objects = 0

    """[Class constructor]
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """[Function create JSON]
        """
        if list_dictionaries is None:
            list_dictionaries = []

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """[Function read JSON]
        """
        new_list = []
        if json_string is None or len(json_string) == 0:
            return new_list
        new_list = json.loads(json_string)
        return new_list

    @classmethod
    def save_to_file(cls, list_objs):
        """[Method save data]
        """
        new_list = []
        file = cls.__name__ + '.json'

        for items in list_objs:
            new_list.append(items.to_dictionary())

        with open(file, mode='w', encoding='utf-8') as file:
            s = json.dumps(new_list)
            file.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """[method create instance]
        """
        if cls.__name__ == 'Square':
            tmp = cls(2)
        elif cls.__name__ == 'Rectangle':
            tmp = cls(1, 2)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """[Method create file]
        """
        file = cls.__name__ + '.json'
        new_list = []
        if not os.path.isfile(file):
            return []
        with open(file, mode='r', encoding='utf-8') as file:
            tmp = Base.from_json_string(file.read())
            new_list = [cls.create(**items) for items in tmp]
            return new_list
