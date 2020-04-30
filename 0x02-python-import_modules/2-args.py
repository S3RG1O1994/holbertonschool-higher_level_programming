#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        print('0 arguments.')
    else:
        print('{} arguments:'.format(len(argv) - 1))
        i = 2
        for i in range(1, len(argv)):
            if argv == 0:
                continue
            else:
                print('{}: {}'.format(i, argv[i]))
