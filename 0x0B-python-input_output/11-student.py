#!/usr/bin/python3
"""class student module"""


class Student:
    """the class"""

    def __init__(self, first_name, last_name, age):
        """intialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a function retrieves a dictionary
            representation of a Student instance.
            If attrs is a list of strings,
            only attribute names contained in this list must be retrieved."""
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """a method that replaces all attributes of the Student"""
        for key, value in json.items():
            setattr(self, key, value)
