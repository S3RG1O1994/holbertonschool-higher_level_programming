#!/usr/bin/python3
"""function is_same_class is for verify an obj.
"""


def is_same_class(obj, a_class):
    """is_same_class

    Arguments:
        obj {object} -- [he can be object of anyone class]
        a_class {class} -- [she can be class of python]

    Returns:
        [boolean] -- [true if obj and a_class be same class or false if not]
    """

    return type(obj) is a_class
