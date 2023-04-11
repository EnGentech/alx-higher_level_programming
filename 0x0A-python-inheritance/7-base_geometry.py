#!/usr/bin/python3
"""A program to check for TypeErrors
and ValueError from input written by
EnGentech"""


class BaseGeometry:
    """defining a class of BaseGeometry"""
    
    def area(self):
        """defining an area function"""
        raise Exceptioni("area() is not implemented")

    def integer_validator(self, name, value):
        """funtion declaration"""
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

# EnGentech sign
