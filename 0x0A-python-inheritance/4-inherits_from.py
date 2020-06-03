#!/usr/bin/python3
"""[Function for discover of that class inherit an object]
"""


def inherits_from(obj, a_class):
    """[inherits_from]

    Arguments:
        obj {[object]} -- [He can be anyone object create]
        a_class {[class]} -- [anything class of python]

    Returns:
        [boolean] -- [true or false]
    """

    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
