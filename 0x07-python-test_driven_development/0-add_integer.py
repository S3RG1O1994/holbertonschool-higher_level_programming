#!/usr/bin/python3
"""
    This function is for print the add within two integer
    this number should be integer or float.

    Return:
            [Int] - [Plus within a, b]
"""


def add_integer(a, b=98):
	"""[add_integer]

    Arguments:
        a {[type]} -- [data should type int]

    Keyword Arguments:
        b {int} -- [data should type int] (default: {98})

    Raises:
        TypeError: [add_integer() missing 1 required positional argument: "a"]
        TypeError: [a must be an integer]
        TypeError: [b must be an integer]

    Returns:
        [int] -- [Plus within a in b]
    """


	if a is None:
		raise TypeError('add_integer() missing 1 required positional argument: "a"')
	if type(a) != int and type(a) != float:
		raise TypeError('a must be an integer')
	if type(b) != int and type(b) != float:
		raise TypeError('b must be an integer')
	return int(a + b)
