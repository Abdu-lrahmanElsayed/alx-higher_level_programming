#!/usr/bin/python3
"""This module to print a square with the character #"""


def print_square(size):
    """function that prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        print()
    else:
        i = 0
        while i < size:
            for j in range(size):
                print("#", end="")
            print()
            i += 1


if __name__ == "__main__":
    import doctest
    doctest.testmethod("tests/4-print_square.txt")
