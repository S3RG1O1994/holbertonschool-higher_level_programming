#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        a = my_list[:]
        return (a)
    elif idx > len(my_list):
        a = my_list.copy()
        return a
    else:
        a = my_list.copy()
        for i in range(len(a)):
            if idx == i:
                a[i] = element
        return a
