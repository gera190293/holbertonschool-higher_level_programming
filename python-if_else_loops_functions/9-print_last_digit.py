#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
        return number % 10
    else:
        return number % 10
