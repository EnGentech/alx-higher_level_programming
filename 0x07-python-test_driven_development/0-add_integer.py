#!/usr/bin/python3
"""A program written to add
the sum of two unknown variables"""


def add_integer(a, b=98):
    """defining a code to add two variables"""
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
