#!/usr/bin/python3
"""A program to return area and perimeter
or a rectangle with extra features"""


class Rectangle:
    """define a class of rectangle with width and height"""
    def __init__(self, width=0, height=0):
        """initializing width and height"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """setting property for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """getting value to height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """getting property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting value to width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """defining formula for area"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """defining formula for perimeter"""
        per = 0
        if self.__width == 0 or self.__height == 0:
            return per
        else:
            per = 2 * (self.__width + self.__height)
            return per

    def __str__(self):
        """return # instead of value"""
        if self.__height != 0 and self.__width != 0:
            i = self.width * "#" + "\n"
            j = self.width * "#"
            return ((self.height - 1) * i + j)
        else:
            return ("")

    def __repr__(self):
        """return the eval of the string instance"""
        exp = "Rectangle({}, {})".format(self.__height, self__width)
        return exp
