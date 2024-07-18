#!/usr/bin/python3
"""A function checks if object is the type of the class using isinstance"""


def is_kind_of_class(obj, a_class):
    """The function

        args:
            obj: is the thing i will check
            a_class: the type"""
    return isinstance(obj, a_class)
