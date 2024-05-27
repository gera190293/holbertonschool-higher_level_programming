#!/usr/bin/python3

"""This is a Python - Input/Output module exercise."""


def write_file(filename="", text=""):
    """Function to write a file and return the number of characters"""
    with open(filename, 'w', encoding="utf-8") as f:
        content = f.write(text)
        c = 0
        content.count(c)
        f.closed
        return c
