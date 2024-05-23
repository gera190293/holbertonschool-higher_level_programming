#!/usr/bin/python3

"""
This module provides utilities for inspecting Python objects.

Functions:
    lookup(obj): Returns a list of available attributes and methods of an object.
"""

def lookup(obj):
    
    """
    Returns the list of available attributes and methods of an object.

    :param obj: The object to inspect.
    :type obj: any
    :return: A list of strings representing the names of the attributes and methods.
    :rtype: list
    """
    
    return dir(obj)
