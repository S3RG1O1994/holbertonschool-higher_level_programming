#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != int and roman_string != None:
        num = 0
        num_romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for pos in range(len(roman_string)):
            if pos == len(roman_string) - 1:
                num += num_romans[roman_string[pos]]
            elif num_romans[roman_string[pos]] >= num_romans[roman_string[pos + 1]]:
                num += num_romans[roman_string[pos]]
            else:
                num -= num_romans[roman_string[pos]]
        return num
    else:
        return 0
