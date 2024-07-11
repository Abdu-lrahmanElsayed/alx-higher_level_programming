#!/usr/bin/python3
"""I will create the same class Square with a size but with vlue and area
    and this time with property for getter and setter"""


class Square:
    """my Square"""

    def __init__(self, size=0):
        """Initializes data

            args:
                size: Private instance attribute with standard value 0"""
        self.__size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter

            args:
                value for size

            raises:
                TypeError: If `size` is not an integer.
                ValueError: If `size` is less than 0."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """A method for erea"""
        return self.__size ** 2

    def __eq__(self, other):
        """check equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """check not equal"""
        return self.area() != other.area()

    def __gt__(self, other):
        """check bigger than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """check bigger than or equal"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """check less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """check less than or equal"""
        return self.area() <= other.area()
