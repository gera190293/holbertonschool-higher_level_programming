#!/usr/bin/python3

"""Abstract Base Classes excercises"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal class"""
    pass
    
    @abstractmethod
    def sound(self):
        """abstract method"""

class dog(Animal):
    """Subclass dog"""
    pass
    
    def sound(self):
        """Sound method"""
        return "Bark"

class cat(Animal):
    """subclass cat"""
    pass

    def sound(self):
        """Sound method"""
        return "Meow"
