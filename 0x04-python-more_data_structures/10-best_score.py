#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    new_value = a_dictionary.values()
    sum = 0
    for value in new_value:
        if sum < value:
            sum = value
    return sum
