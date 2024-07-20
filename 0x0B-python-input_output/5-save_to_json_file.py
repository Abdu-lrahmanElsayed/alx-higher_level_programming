#!/usr/bin/python3
"""a function that writes an Object to a json file"""


import json


def save_to_json_file(my_obj, filename):
    """the function"""
    txt = json.dumps(my_obj)
    with open(filename, 'w', encoding="UTF8") as f:
        f.write(txt)
