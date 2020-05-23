#!/usr/bin/python3
"""
    say_my_name is an function for print only first_name and last_name
"""


def say_my_name(first_name, last_name=""):
    """[say_my_name]

    Arguments:
        first_name {[str]} -- [string]

    Keyword Arguments:
        last_name {str} -- [string] (default: {""})

    Raises:
        TypeError: [say_my_name() missing 1 required
        positional argument: 'first_name]
        TypeError: [first_name must be a string]
        TypeError: [last_name must be a string]
    """
    e = "say_my_name() missing 1 required positional argument: 'first_name'"
    if not first_name:
        raise TypeError(e)
    if type(first_name) != str or len(first_name) <= 1:
        raise TypeError('first_name must be a string')
    if type(last_name) != str or len(last_name) == 1:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name), sep=" ")
