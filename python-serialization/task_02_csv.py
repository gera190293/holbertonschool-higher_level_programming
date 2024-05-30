#!/usr/bin/python3

"""This is a Python - Serialization module exercise"""
import csv
import json


def convert_csv_to_json(filename):
    """Takes the CSV filename as its parameter and writes the JSON"""
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            r = csv.DictReader(f)
            data = [row for row in r]

        with open('r.jason', mode='w', encoding='utf-8') as jf:
            json.dump(data, jf, indent=4)
        return True
    except FileNotFoundError:
        return False
