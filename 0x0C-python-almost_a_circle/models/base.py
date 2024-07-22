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

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method that:
        writes the JSON string representation of list_objs to a file
        list_objs is a list of instances who inherits of Base"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        json_txt = cls.to_json_string(list_objs)
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="UTF8") as f:
            f.write(json_txt)

    @staticmethod
    def from_json_string(json_string):
        """a static method that:
        returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
