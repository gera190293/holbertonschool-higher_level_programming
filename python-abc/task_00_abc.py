#!/usr/bin/python3

"""Abstract Base Classes exercises"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal class"""

    @abstractmethod
    def sound(self):
        """Abstract method to define animal sounds"""
        pass

class Dog(Animal):
    """Subclass Dog"""

    def sound(self):
        """Sound method"""
        return "Bark"

class Cat(Animal):
    """Subclass Cat"""

    def sound(self):
        """Sound method"""
        return "Meow"
