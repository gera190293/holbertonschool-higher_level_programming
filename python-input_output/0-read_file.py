#!/usr/bin/python3

"""This is a Python - Input/Output module exercises"""

def read_file(filename=""):
    """Function to read a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        filename = f.read()
        print(filename)
        f.closed