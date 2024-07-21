#!/usr/bin/python3
"""A module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method should return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )
