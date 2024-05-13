#!/usr/bin/python3

def chklen(tuple_x=()):
    if len(tuple_x) >= 2:
        return tuple_x
    elif len(tuple_x) == 1:
        newt = (tuple_x[0], 0)
        return newt
    else:
        newt = (0, 0)
        return newt


def add_tuple(tuple_a=(), tuple_b=()):
    t_a = tuple(chklen(tuple_a))
    t_b = tuple(chklen(tuple_b))
    a = t_a[0] + t_b[0]
    b = t_a[1] + t_b[1]
    new_tuple = (a, b)
    return new_tuple
