#!/usr/bin/python3
def uppercase(str):
    for n in str:
        print("{}" .format(ord(n - 32), end=""))
