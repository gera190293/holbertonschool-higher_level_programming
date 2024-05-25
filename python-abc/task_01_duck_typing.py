#!/usr/bin/python3

"""Abstract Base Classes exercises"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape class"""

    @abstractmethod
    def area(self):
        """abstract area method"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """abstract perimeter method"""
        pass


class Circle(Shape):
    """Circle class inheritance from shape"""

    def __init__(self, radius):
        """set attributes for Circle"""
        self.radius = radius

    def area(self):
        """area method with radius"""
        return math.pi * (self.radius ** 2)

    def area(self):
        """area method with perimeter"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheritance from shape"""

    def __init__(self, width, height):
        """set attributes for Rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """area method for Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """perimeter method for Rectangle"""
        return 2 * (self.width + self.height)
