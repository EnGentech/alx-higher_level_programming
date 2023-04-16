#!/usr/bin/python3
"""A program written by EnGentech to
define Rectangle as a class inherited
from Base pre written"""

from models.base import Base


class Rectangle(Base):
    """defining a class for Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing stage"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val

    def area(self):
        """function to find rectangular area"""

        area = self.__height * self.__width
        return area

    def display(self):
        """function to print # depending on input"""

        print("\n"*self.__y, end="")
        for i in range(self.__height):
            print(' '*self.__x + "#"*self.__width)

    def __str__(self):
        """function to overwrite an instance using __str__"""

        strOut = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)
        return strOut

    def update(self, *args, **kwargs):
        """function to implement args dn kwargs"""

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """function to add to dictionary"""

        x = self.x
        y = self.y
        i = self.id
        h = self.height
        w = self.width
        my_dict = {"x": x, "y": y, "id": i, "height": h, "width": w}
        return my_dict

# EnGentech sign
