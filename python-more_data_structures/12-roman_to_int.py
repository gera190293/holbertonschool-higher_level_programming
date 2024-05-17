#!/usr/bin/python3

def roman_to_int(roman_string):
    def roman_value(symbol):
        if symbol == "M":
            return 1000
        elif symbol == "D":
            return 500
        elif symbol == "C":
            return 100
        elif symbol == "L":
            return 50
        elif symbol == "X":
            return 10
        elif symbol == "V":
            return 5
        else:
            return 1

    number = 0
    if roman_string == "" or not isinstance(roman_string, str):
        return 0
    else:
        for i in range(len(roman_string)):
            current_value = roman_value(roman_string[i])
            if i < len(roman_string) - 1 and current_value < roman_value(roman_string[i + 1]):
                number -= current_value
            else:
                number += current_value
    return number
