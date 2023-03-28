#!/usr/bin/python3
"""defining a class of square with
a function to print area of a square"""


class Square:
    """defining the class of square"""
    __size = None

    def __init__(self, size=0):
        """initializing size as a must int"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """formula to calculate the area of a square"""
        area_of_a_square = self.__size**2
        return area_of_a_square
