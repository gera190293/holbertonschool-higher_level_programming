#!/usr/bin/python3

def print_list_integer(my_list=[]):
    n = 0
    for n in range(len(my_list)):
        if n == len(my_list) - 1:
            print("{:d}".format(my_list[n]), end="")
        else:
            print("{:d}".format(my_list[n]), end=" ")
    return ""


def print_matrix_integer(matrix=[[]]):
    n = 0
    for n in range(len(matrix)):
        print("{}".format(print_list_integer(matrix[n])))
