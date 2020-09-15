#!/usr/bin/python3
'''Function for find peak in the list_of_integers'''


def find_peak(list_of_integers):
    '''search peak'''

    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
