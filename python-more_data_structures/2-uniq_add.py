#!/usr/bin/python3

def uniq_add(my_list=[]):
    if not my_list:
        return None
    total = 0
    for n in set(my_list):
        total += n
    return total
