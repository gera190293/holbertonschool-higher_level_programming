#!/usr/bin/python3

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    :param obj: The object to inspect
    :return: A list of strings representing the names of the attributes and methods
    """
    return dir(obj)
