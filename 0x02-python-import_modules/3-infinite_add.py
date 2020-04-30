#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        print('{}'.format(len(argv) - 1))
    else:
        aux = 0
        for i in range(1, len(argv)):
            aux += int(argv[i])
        print(aux)
