#!/usr/bin/python3
"""[Function for save an object in an file-text]
"""

import json


def save_to_json_file(my_obj, filename):
    """create JSON"""

    with open(filename, mode='a', encoding='utf-8') as file:
        json.dump(my_obj, file)
