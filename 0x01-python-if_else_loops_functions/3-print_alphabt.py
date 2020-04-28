#!/usr/bin/python3
for w in range(97, 123):
    if (w == 101 or w == 113):
        continue
    else:
        print('{:c}'.format(w), end="")
