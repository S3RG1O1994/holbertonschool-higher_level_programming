#!/usr/bin/python3
for w in range(100):
    if w == 99:
        print('{:02d}'.format(w))
    else:
        print('{:02d}, '.format(w), end="")
