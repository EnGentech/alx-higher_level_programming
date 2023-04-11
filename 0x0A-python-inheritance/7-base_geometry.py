#!/usr/bin/python3
"""A program to check for TypeErrors
and ValueError from input written by
EnGentech"""


class BaseGeometry:
    """BaseGeometry class defined"""

    def area(self):
        """this is a method for area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating integer input"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
