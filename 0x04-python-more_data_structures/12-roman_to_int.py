#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str and roman_string is None:
        return 0
    num = 0
    num_romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            num += num_romans[roman_string[i]]
        elif num_romans[roman_string[i]] >= num_romans[roman_string[i + 1]]:
            num += num_romans[roman_string[i]]
        else:
            num -= num_romans[roman_string[i]]
    return num
