#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    return tuple(sum(pair) for pair in zip(tuple_a + (0, 0), tuple_b + (0, 0)))
