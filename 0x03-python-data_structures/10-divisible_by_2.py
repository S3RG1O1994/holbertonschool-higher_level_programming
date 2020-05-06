#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy = my_list.copy()
    length = len(copy)
    for i in range(0, length):
        if my_list[i] % 2 == 0:
            copy[i] = True
        else:
            copy[i] = False
    return copy
