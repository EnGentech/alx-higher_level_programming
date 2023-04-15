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
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val
# EnGentech sign