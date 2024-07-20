#!/usr/bin/python3
"""class student module"""


class Student:
    """the class"""

    def __init__(self, first_name, last_name, age):
        """intialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a function retrieves a dictionary
        representation of a Student instance"""
        return self.__dict__
