#!/usr/bin/python3

class Mylist(list):
    """
    A subclass of list
    """
    
    
    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))