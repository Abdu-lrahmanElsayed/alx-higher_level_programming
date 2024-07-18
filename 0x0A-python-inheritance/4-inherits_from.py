#!/usr/bin/python3
"""a function that returns True
    if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """The function

        args:
            obj: is the thing i will check
            a_class: the inherited class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
