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
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        """area method with radius"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """perimeter method with radius"""
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


def shape_info(shape):
    """print the info of the shape"""
    try:
        area = shape.area()
        perimeter = shape.perimeter()
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
    except AttributeError:
        print("The provided shape does not implement required methods.")
