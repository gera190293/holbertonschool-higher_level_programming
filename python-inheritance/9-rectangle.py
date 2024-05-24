#!/usr/bin/python3

"""
This module provides the Rectangle class inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a class Rectangle from BaseGeometric"""


    def __init__(self, width, height):
        """Check if width and height was integers with integer_validator"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


    def __str__(self):
        """Str behavior"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


    def area(self):
        """Function that return the area of the rectangle"""
        return self.__height * self.__width
