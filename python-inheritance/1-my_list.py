#!/usr/bin/python3

"""
This module provides utilities for inspecting Python objects.
"""


class Mylist(list):
    """
    A subclass of list
    """
    
    
    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(int(sorted(self)))