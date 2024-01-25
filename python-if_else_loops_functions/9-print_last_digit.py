#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print("{}".format(abs(number) % 10))
    else:
        print("{}".format(number % 10))
