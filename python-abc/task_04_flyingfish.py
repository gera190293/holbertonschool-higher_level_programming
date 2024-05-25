#!/usr/bin/python3

"""Abstract Base Classes exercises"""


class Fish():
    """Fish class"""

    def swim(self):
        """Method for fish to swim"""
        return "The fish is swimming"

    def habitat(self):
        """Method for fish for habitat"""
        return "The fish lives in water"


class Bird():
    """Bird class"""

    def fly(self):
        """Method for bird to fly"""
        return "The bird is flying"

    def habitat(self):
        """Method for bird to fly"""
        return "The bird lives in the sky"


class FlyingFish(Bird, Fish):
    """Flyingfish class that inherits from both Fish and Bird"""

    def swim(self):
        """Method for fish to swim"""
        return "The flying fish is swimming!"

    def habitat(self):
        """Method for fish for habitat"""
        return "The flying fish lives both in water and the sky!"

    def fly(self):
        """Method for bird to fly"""
        return "The flying fish is soaring!"
