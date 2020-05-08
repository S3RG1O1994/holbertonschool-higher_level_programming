#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for items, value in a_dictionary.items():
        new_dic[items] = value * 2
    return new_dic
