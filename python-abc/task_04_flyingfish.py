#!/usr/bin/python3

"""Abstract Base Classes exercises"""


class Fish():
    """Fish class"""

    def swim(self):
        """Method for fish to swim"""
        print("The fish is swimming")

    def habitat(self):
        """Method for fish for habitat"""
        print("The fish lives in water")


class Bird():
    """Bird class"""

    def fly(self):
        """Method for bird to fly"""
        print("The bird is flying")

    def habitat(self):
        """Method for bird to fly"""
        print("The bird lives in the sky")


class FlyingFish(Bird, Fish):
    """Flyingfish class that inherits from both Fish and Bird"""

    def swim(self):
        """Method for fish to swim"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Method for fish for habitat"""
        print("The flying fish lives both in water and the sky!")

    def fly(self):
        """Method for bird to fly"""
        print("The flying fish is soaring!")
