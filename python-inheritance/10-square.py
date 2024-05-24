#!/usr/bin/python3

"""
This module provides the Square class which inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class based on Rectangle class."""

    def __init__(self, size):
        """
        Initialize a new Square instance
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size ** 2
