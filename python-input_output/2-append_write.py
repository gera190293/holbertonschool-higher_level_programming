#!/usr/bin/python3

"""This is a Python - Input/Output module exercise."""


def append_write(filename="", text=""):
    """Function to append a file and return
    the number of characters written"""
    with open(filename, 'a', encoding="utf-8") as f:
        appen = f.write(text)
        return appen
