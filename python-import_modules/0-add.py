#!/usr/bin/python3
import add_0 as plus_0
def sum():
    a = 1
    b = 2
    c = plus_0.add(a, b)
    print("{} + {} = {}".format(a, b, c))

if __name__ == '__main__':
    sum()
