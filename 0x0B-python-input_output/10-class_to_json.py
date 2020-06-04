#!/usr/bin/python3
"""[function that copy an instance]
"""


def class_to_json(obj):
    dir = {}
    if hasattr(obj, "__dict__"):
        dir = obj.__dict__.copy()
    return dir
