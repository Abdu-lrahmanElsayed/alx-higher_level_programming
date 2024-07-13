#!/usr/bin/python3
"""This module 0-add_integer
    is to add 2 integers
    and raise error if something is wrong
    and check doctest cases
    it returns addition as add of the 2 integers"""


def add_integer(a, b=98):
    """add function to add integer a to b
        rases:
            TypeError if a or b are not integers"""
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    addition = a + b
    return addition


if __name__ == "__main__":
    import doctest
    doctest.testmethod("tests/0-add_integer.txt")
