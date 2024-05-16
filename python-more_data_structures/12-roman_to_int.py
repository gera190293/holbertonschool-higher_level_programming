#!/usr/bin/python3

def sum(n):
    if n == "M":
        return 1000
    elif n == "D":
        return 500
    elif n == "C":
        return 100
    elif n == "L":
        return 50
    elif n == "X":
        return 10
    elif n == "V":
        return 5
    else:
        return 1


def roman_to_int(roman_string):
    number = 0
    if roman_string == "" or type(roman_string) != str:
        return 0
    else:
        for i in range(len(roman_string)):
            rc = roman_string[i]
            rv = sum(rc)
            if i < len(roman_string) - 1 and rv < sum(roman_string[i + 1]):
                number -= rv
            else:
                number += rv
    return number
