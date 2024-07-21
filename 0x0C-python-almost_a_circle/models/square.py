#!/usr/bin/python3
"""A module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """method should return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )

    def update(self, *args, **kwargs):
        """a public method that assigns an argument to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
