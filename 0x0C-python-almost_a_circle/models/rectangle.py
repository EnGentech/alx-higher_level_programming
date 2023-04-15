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

        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
# EnGentech sign
