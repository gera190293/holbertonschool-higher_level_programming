#!/usr/bin/python3
"""class Square based on 1-square.py"""


class Square:
    """Square class"""
    
    def __init__(self, size=0):
        """Initialize a new Square.
        
        Args:
        size (int): Size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
