#!/usr/bin/python3
"""[Function for add string in the last of an file]
"""


def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
