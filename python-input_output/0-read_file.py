#!/usr/bin/python3

"""This is a Python - Input/Output module exercise."""


def read_file(filename=""):
    """Function to read a file and print its contents."""
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
