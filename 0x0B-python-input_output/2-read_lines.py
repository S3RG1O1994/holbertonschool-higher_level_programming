#!/usr/bin/python3
"""[Function for print an determinate number of lines of an file]
"""


def read_lines(filename="", nb_lines=0):
    with open(filename, mode='r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read())
        else:
            for i in range(nb_lines):
                print(f.readline())
