#!/usr/bin/python3

"""This is a Python - Serialization module exercise"""
import pickle


class CustomObject():
    """Class definition for CustomObject"""
    def __init__(self, name, age, is_student):
        """Constructor for CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance of the object"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except PermissionError:
            print(f"Error: Permission denied to write to the file '{filename}'.")
        except pickle.PicklingError:
            print(f"Error: The object could not be serialized.")

    @classmethod
    def deserialize(cls, filename):
        """Will load and return an instance of the CustomObject
        from the provided filename"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print(f"The file '{filename}' was not found.")
        except PermissionError:
            print(f"Permission denied to read the file '{filename}'.")
        except pickle.UnpicklingError:
            print(f"The file '{filename}' does not contain a valid serialized object.")
        except EOFError:
            print(f"The file '{filename}' is empty or corrupted.")
        except AttributeError:
            print(f"The class definition required for deserialization is missing.")
