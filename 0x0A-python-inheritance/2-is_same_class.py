#!/usr/bin/python3
"""A function checks if object is the type of the class"""


def is_same_class(obj, a_class):
    """The function

        args:
            obj: is the thing i will check
            a_class: the type"""
    return type(obj) == a_class
