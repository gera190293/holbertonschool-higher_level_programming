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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in
        this list will be retrieved. Otherwise,
        all attributes will be retrieved.

        Args:
            attrs (list, optional): List of attribute names to include in the
            dictionary representation. Defaults to None.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return {key: value for key, value in self.__dict__.items()
                if isinstance(value, (list, dict, str, int, bool))}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from json.

        Args:
            json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
