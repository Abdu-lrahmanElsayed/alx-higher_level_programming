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
        self.__size = size
        self.__position = position

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
        if type(vlaue) is tuple:
            if len(value) == 2:
                for i in value:
                    if isinstance(i, int) or i >= 0:
                        self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """area method"""
        return self.__size ** 2

    def my_print(self):
        """public method to print a square of # in stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
            for i in range(self.__position[1]):
                print()
