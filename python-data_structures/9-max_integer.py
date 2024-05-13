#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        n = 0
        m = my_list[0]
        for n in range(len(my_list) - 1):
            if m <= my_list[n + 1]:
                m = my_list[n + 1]
            else:
                m = m
        return m
