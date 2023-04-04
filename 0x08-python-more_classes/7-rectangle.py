#!/usr/bin/python3
"""A program to print strings
base on user input"""


class Rectangle:
    """define a class of rectangle with width and height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing width and height"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            i = self.width * "{0!s}".format(self.print_symbol) + "\n"
            j = self.width * "{0!s}".format(self.print_symbol)
            return ((self.height - 1) * i + j)
        else:
            return ("")

    def __repr__(self):
        """return the instance string as given"""
        exp = "Rectangle({}, {})". format(self.__width, self.__height)
        return exp

    def __del__(self):
        """if an instance of delete occurs, print a message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
