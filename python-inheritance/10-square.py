#!/usr/bin/python3

"""
This module provides the Square class inherits from Rectangle
"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Square class based on Rectangle class"""
    
    def __init__(self, size):
        """Check if size is an integer"""
        self.integer_validation("size", size)
        self.__size__ = size

    def area(self):
        """Calculate the area of a square"""
        return self.__size__ ** 2
