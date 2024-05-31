#!/usr/bin/python3

"""This is a Python - Serialization module exercise"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary into XML
    and saves it to the given filename."""
    try:
        root = ET.Element("data")
  
        def add_elements(parent, dict_obj):
            for key, value in dict_obj.items():
                child = ET.SubElement(parent, key)
                if isinstance(value, dict):
                    add_elements(child, value)
                else:
                    child.text = str(value)

        add_elements(root, dictionary)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"An error ocurred with {e}")
        return False

def deserialize_from_xml(filename):
    """Deserializes XML data from the given
    filename and returns a Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        def parse_element(element):
            parsed_dict = {}
            for child in element:
                if len(child):
                    parsed_dict[child.tag] = parse_element(child)
                else:
                    parsed_dict[child.tag] = child.text
            return parsed_dict
        return parse_element(root)
    except (FileNotFoundError, ET.ParseError):
        print("An error has ocurred")
        return None
