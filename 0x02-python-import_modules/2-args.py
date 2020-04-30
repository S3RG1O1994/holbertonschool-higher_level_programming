#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('0 arguments.')
    else:
        print('{} arguments:'.format(len(sys.argv) - 1))
        i = 2
        for i in range(1, len(sys.argv)):
            if sys.argv == 0:
                continue
            else:
                print('{}: {}'.format(i, sys.argv[i]))
