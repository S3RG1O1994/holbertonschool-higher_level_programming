#!/usr/bin/python3
"""[Function for read an JSON as string]

Returns:
    [type] -- [description]
"""

import json


def from_json_string(my_str):
    """Function create obj"""

    zaz = json.loads(my_str)
    return zaz
