#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for i in my_list:
        if i == search:
            copy.insert(i, replace)
        else:
            copy.append(i)
    return copy
