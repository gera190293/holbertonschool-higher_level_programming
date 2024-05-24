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
