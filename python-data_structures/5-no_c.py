#!/usr/bin/python3

def cremove(c):
    if ord(c) == 67 or ord(c) == 99:
        return ""
    else:
        return c


def no_c(my_string):
    new_string = list(my_string)
    for n in range(len(new_string)):
        new_string[n] = cremove(new_string[n])
    return ''.join(new_string)
