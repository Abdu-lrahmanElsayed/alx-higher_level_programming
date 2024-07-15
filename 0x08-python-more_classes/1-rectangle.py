#!/usr/bin/python3
"""My reactangle class"""


class Rectangle:
    """A reactangle with width and height"""

    def __init__(self, width=0, height=0):
        """Initializes data

            args:
                width with standard value 0.
                height with standard value 0.
                """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

            raises:
                TypeError: if width is not integer.
                ValueError: if width is less than 0.
                """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

            raises:
                TypeError: if height is not integer.
                ValueError: if height less than 0.
                """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
