#!/usr/bin/python3

"""
This module provides utilities for inspecting Python objects.
"""


class MyList(list):
    
    """
    A subclass of list
    
     Methods:
        print_sorted(self):
            Prints the list in ascending order.
    """
    
    
    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))
        