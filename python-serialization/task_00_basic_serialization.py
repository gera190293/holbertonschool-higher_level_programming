#!/usr/bin/python3

"""This is a Python - Serialization module exercise"""
import pickle


def serialize_and_save_to_file(data, filename):
    """Function that serialize and save data to the specified file"""
    with open(filename, 'w', encoding="utf-8") as f:
        pickle.dump(data, f)

def load_and_deserialize(filename):
    """Function that load and deserialize data from a specified file"""
    with open(filename, "r", encoding="utf-8") as f:
        return pickle.load(f)
