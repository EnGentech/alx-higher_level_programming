#!/usr/bin/python3
"""A class of square with raise value and type error"""


class Square:
    """defining conditions for size"""
    __size = None

    def __init__(self, size=0):
        """initiallizing conditions for size"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
