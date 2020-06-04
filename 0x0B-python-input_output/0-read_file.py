#!/usr/bin/python3
"""[read_file is function for print the contain of an file]
"""


def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read())
