#!/usr/bin/python3
"""A class to try magic methods"""


class MyInt(int):
    """the class inherited from int"""

    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
