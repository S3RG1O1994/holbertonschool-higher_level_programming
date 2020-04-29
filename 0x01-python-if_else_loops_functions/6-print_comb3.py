#!/usr/bin/python3
for w in range(0, 9):
    for i in range(10):
        if i <= w:
            continue
        else:
            if w < 8:
                print('{}{}, '.format(w, i), end="")
            else:
                print('{}{}'.format(w, i))
