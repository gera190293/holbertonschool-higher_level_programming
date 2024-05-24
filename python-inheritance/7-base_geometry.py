#!/usr/bin/python3

"""
This module provides the BaseGeometry class.
"""


class BaseGeometry:
    """A class representing geometric shapes."""

    def area(self):
        """
        Public instance method to calculate area.

        Raises:
            Exception: Indicates that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method to validate if value is an int"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
