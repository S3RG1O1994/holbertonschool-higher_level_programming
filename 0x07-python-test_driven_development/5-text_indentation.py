#!/usr/bin/python3
"""[text_indentation] is an function for print one string
"""


def text_indentation(text):
    """[text_indentation]

    Arguments:
        text {[str]} -- [string]

    Raises:
        TypeError: [text_indentation() missing 1
        required positional argument: 'text']
        TypeError: [text must be a string]
    """

    e = "text_indentation() missing 1 required positional argument: 'text'"
    if text is None:
        raise TypeError(e)
    if type(text) is not str or len(text) <= 1:
        raise TypeError('text must be a string')
    for c in text:
        if c != '.' and c != '?' and c != ':':
            print('{}'.format(c), end="")
        else:
            print('{}\n'.format(c))
