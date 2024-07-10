#!/usr/bin/python3
"""I will create the same class Square with a size but with vlue"""


class Square:
    """My class Square"""

    def __init__(self, size=0):
        """Initializes data

            args:
                size: Private instance attribute with standard value 0
            raises:
                TypeError: If `size` is not an integer.
                ValueError: If `size` is less than 0."""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
