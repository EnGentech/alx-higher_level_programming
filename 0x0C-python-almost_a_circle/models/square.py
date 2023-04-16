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

    def update(self, *args, **kwargs):
        """defining function to setattr using kwargs"""

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """function to define dictionary"""

        x = self.x
        y = self.y
        s = self.size
        id = self.id
        my_dict = {"id": id, "x": x, "size": s, "y": y}
        return my_dict

# EnGentech sign
