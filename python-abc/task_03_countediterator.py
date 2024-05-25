#!/usr/bin/python3

"""Abstract Base Classes exercises"""


class CountedIterator:
    """Iterator class that counts the number of items iterated"""

    def __init__(self, iterable):
        """Initialize with an iterable and set up the iterator and counter"""
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """Return the iterator object itself"""
        return self

    def __next__(self):
        """Return the next item and increment the counter"""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return the current value of the counter"""
        return self.counter
