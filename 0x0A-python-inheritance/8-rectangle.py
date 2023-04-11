#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""A program to inherit a class of rectangle
from BaseGeometry written by EnGentech"""


class Rectangle(BaseGeometry):
    """defining class Rectangle"""

    def __init__(self, width, height):
        """defining function for rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        # EnGentech sign
