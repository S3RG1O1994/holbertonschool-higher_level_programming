#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = my_list.copy()
    for i in range(len(copy)):
        if i == search:
            copy.pop(i)
            copy.insert(i, replace)
    return copy
