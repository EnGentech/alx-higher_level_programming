#!/usr/bin/python3
"""A program to inherit a class of rectangle
from BaseGeometry written by EnGentech"""


class BaseGeometry:
    """defining geometry same as task 7"""

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) is not int:

            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")

    def area(self):
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """defining class Rectangle"""

    def __init__(self, width, height):
        """defining function for rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        # EnGentech sign
