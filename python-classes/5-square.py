#!/usr/bin/python3
"""class Square based on 2-square.py"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialize a new Square.
        
        Args:
        size (int): Size of the square
        """
        self.size = size

    @property
    def size (self):
        """Get/set size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance for area"""
        
        return self.__size ** 2

    def my_print(self):
        """Public instance for print square"""
        if self.__size == 0:
            print("")
        else:
            i = 0
            while i < self.__size:
                    n = "#" * self.__size
                    print(n)
                    i += 1
