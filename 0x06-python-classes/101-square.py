#!/usr/bin/python3
"""I will create the same class Square
    with a size with value and area and position
    and this time with property for getter and setter
    this time will asquare of # """


class Square:
    """My Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes data

            args:
                size: Private instance attribute with standard value 0
                position: private instance attribute of atuple
                """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter

            args:
                value for position

                raises:
                    TypeError: If position
                    is not a tuple of 2 positive integers
                    """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """area method"""
        return self.__size ** 2

    def __str__(self):
        """public method to print a square of # in stdout"""
        if self.__size == 0:
            return '\n'
        else:
            result = ""
            for i in range(self.__position[1]):
                result += '\n'
            for j in range(self.__size):
                result += " " * self.__position[0] + ("#" * self.__size)
                if j != self.__size - 1:
                    result += '\n'
            return result
