#!/usr/bin/python3
import hidden_4 as hidden
if __name__ == '__main__':
    list = dir(hidden)
    for i in list:
        if i[:2] != '__':
            print(i)
