#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, 'w', encoding="utf-8") as f:
        filename = f.read()