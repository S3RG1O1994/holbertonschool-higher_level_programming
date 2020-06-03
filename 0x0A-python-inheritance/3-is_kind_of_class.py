#!/usr/bin/python3
"""function for verify an object if instance of an class or the an superclass
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class

    Arguments:
        obj {[object]} -- [he can be object of anyone class]
        a_class {[class]} -- [she can be anyone class of python]

    Returns:
        [boolean] -- [true or false]
    """

    return isinstance(obj, a_class)
