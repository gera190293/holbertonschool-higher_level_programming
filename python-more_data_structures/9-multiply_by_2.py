#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = {}
    m = 0
    for n in set(a_dictionary):
        m = a_dictionary[n] * 2
        new_dic[n] = m
    return new_dic
