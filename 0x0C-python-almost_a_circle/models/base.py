#!/usr/bin/python3
"""The Base class modul"""
import json


class Base:
    """Base class
        private class attribute __nb_objects = 0"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize attricutes

            args: id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method that returns:
        the JSON string representation of list_dictionaries
        list_dictionaries is a list of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
