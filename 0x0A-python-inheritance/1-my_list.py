#!/usr/bin/python3
"""subclass myList contain an function for print one list sorted
"""


class MyList(list):
    """print_sorted print an list in sorted

    Arguments:
        list {list} -- [superclass list of python]
    """

    def print_sorted(self):
        """Print list sorted"""
        print(sorted(self))
