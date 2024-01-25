#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        m = 1
        for n in range(b):
            m *= a
        return m
    else:
        m = 1.0
        for n in range(abs(b)):
            m /= a
        return m
