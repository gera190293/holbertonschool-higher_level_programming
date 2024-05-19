#!/usr/bin/python3
"""class Square based on 2-square.py"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        
        Args:
        size (int): Size of the square
        position (tuple): Position in the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        """Get/set position in square"""
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

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
                m = " " * self.__position[0]
                n = "#" * self.__size
                print(f"{m}", end="")
                print(n)
                i += 1
