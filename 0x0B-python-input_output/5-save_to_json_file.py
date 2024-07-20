#!/usr/bin/python3
"""a function that writes an Object to a json file"""


import json


def save_to_json_file(my_obj, filename):
    """the function"""
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
