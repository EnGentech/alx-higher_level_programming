#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""A program to inherits a class written by EnGentech
"""


class Rectangle(BaseGeometry):
    """Class definition for BaseGeometry"""

    def __init__(self, width, height):
        """Method for initialisation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """finding the area"""

        x = self.__width * self.__height
        return x

    def __str__(self):
        """__str__ method declaration"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
