#!/usr/bin/python3
'''Function for find peak in the list_of_integers'''


def find_peak(list_of_integers):
    '''search peak'''

    if not list_of_integers:
        return None
    peak = 0
    for items in list_of_integers:
        if items > peak:
            peak = items
    return peak
