#!/usr/bin/python3
"""[function for create an JSON of an object]

Returns:
    [file] -- [JSON]
"""

import json


def to_json_string(my_obj):
    """Create JSON"""

    j = json.dumps(my_obj)
    return j
