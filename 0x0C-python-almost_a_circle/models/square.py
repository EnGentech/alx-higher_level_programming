#!/usr/bin/python3

from models.rectangle import Rectangle

"""A program written by EnGentech to inherit
the class of Rectangle pre-written"""


class Square(Rectangle):
    """defining a class for Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """function to overwrite an instance using __str__"""

        strOut = "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)
        return strOut

# EnGentech sign
