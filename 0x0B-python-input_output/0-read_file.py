#!/usr/bin/python3
"""[read_file is function for print the contain of an file]
"""


def read_file(filename=""):
    """[reads a text file]"""

    with open(filename, mode="r", encoding="utf-8") as file:
        prt = file.read()
        print(prt, end='')
