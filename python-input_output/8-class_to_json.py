#!/usr/bin/python3

"""This is a Python - Input/Output module exercise."""


def class_to_json(obj):
    """Write a function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    if hasattr(obj, '__dict__'):
        return {key: value for key, value in obj.__dict__.items()
                if isinstance(value, (list, dict, str, int, bool))}
