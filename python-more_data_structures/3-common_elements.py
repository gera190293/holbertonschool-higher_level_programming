#!/usr/bin/python3

def common_elements(set_1, set_2):
    j = 0
    new_set = []
    for m in set_1:
        for j in range(len(set_2)):
            if set_1[j] == set_2[j]:
                n = set_1[j]
                new_set.append(n)
            else:
                continue
    return new_set