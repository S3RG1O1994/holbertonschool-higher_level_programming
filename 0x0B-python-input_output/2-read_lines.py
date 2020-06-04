#!/usr/bin/python3
"""[Function for print an determinate number of lines of an file]
"""


def read_lines(filename="", nb_lines=0):
    """[Function for read an number of lines]"""

    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        if nb_lines <= 0 or nb_lines >= len(lines):
            for i in lines:
                print(i, end='')
        else:
            lines = lines[0: nb_lines]
            for i in lines:
                print(i, end='')
