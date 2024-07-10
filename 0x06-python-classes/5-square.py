#!/usr/bin/python3
"""I will create the same class Square with a size but with vlue and area
    and this time with property for getter and setter
    this time will asquare of #"""


class Square:
    """My Square"""

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
        """area method"""
        return self.__size ** 2

    def my_print(self):
        """public method to print a square of #"""
        if self.__size == 0:
            print()
        else:
            i = 0
            while i < self.__size:
                for j in range(0, self.__size):
                    print("#", end="")
                print()
                i += 1
