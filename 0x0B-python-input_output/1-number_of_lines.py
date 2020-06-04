#!/ur/bin/python3
"""[Function for print number lines in an file]
"""


def number_of_lines(filename=""):
    """[number of lines in the file]"""

    with open(filename, mode='r') as file:
        lines = len(file.readlines())
    return lines
