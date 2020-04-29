#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        copy = ord(str[i])
        if (copy > 96 and copy < 123):
            copy -= 32
        print('{:c}'.format(copy), end="")
    print()
