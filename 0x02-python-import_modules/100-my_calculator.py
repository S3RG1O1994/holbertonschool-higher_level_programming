#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    opr = {'+', '-', '*', '/'}
    if len(argv) < 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif argv[2] in opr:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            print('{} {} {} = {}'.format(a, argv[2], b, add(a, b)))
        elif argv[2] == '-':
            print('{} {} {} = {}'.format(a, argv[2], b, sub(a, b)))
        elif argv[2] == '*':
            print('{} {} {} = {}'.format(a, argv[2], b, mul(a, b)))
        else:
            print('{} {} {} = {}'.format(a, argv[2], b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)