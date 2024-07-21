#!/usr/bin/python3
"""The Base class modul"""


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
