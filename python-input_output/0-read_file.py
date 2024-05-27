#!/usr/bin/python3

"""This is a Python - Input/Output module exercises"""

def read_file(filename=""):
    """Function to read a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        f.read()
        f.closed
