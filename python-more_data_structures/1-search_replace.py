#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if not my_list:
        return None
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            n = int(my_list[i])
            new_list.append(n)
    return new_list
