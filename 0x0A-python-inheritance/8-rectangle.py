#!/usr/bin/python3
"""A program to inherit a class of rectangle
from BaseGeometry written by EnGentech"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defining class Rectangle"""

    def __init__(self, width, height):
    """defining function for rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
# EnGentech sign
