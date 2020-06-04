#!/usr/bin/python3
"""[Function for create an object of an JSON]

Returns:
    [obj] -- [JSON]
"""

import json


def load_from_json_file(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
