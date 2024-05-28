#!/usr/bin/python3

"""
This module defines a Student class with methods for JSON serialization.
"""


class Student:
    """Represents a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        This method returns a dictionary containing all attributes of the
        Student instance that are of a simple data structure type (list, dict,
        string, integer, or boolean).

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return {key: value for key, value in self.__dict__.items()
                if isinstance(value, (list, dict, str, int, bool))}
