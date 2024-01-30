#!/usr/bin/python3

def uniq_add(my_list=[]):
    if not my_list:
        return None
    total = 0
    for n in range(len(my_list) - 1):
        total += int(my_list[n])
    return total
