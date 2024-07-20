#!/usr/bin/python3
""" a function that returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """the function"""
    json_str = json.dumps(my_obj)
    return json_str
