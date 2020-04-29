#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    final = (number * -1) % 10 * -1
else:
    final = number % 10
print('Last digit of {} is {} and is '.format(number, final), end="")
if final > 5:
    print('greater than 5')
elif final == 0:
    print('0')
else:
    print('less than 6 and not 0')
