#!/usr/bin/python3
"""A program to returns the retrival of
json dictionary representation using attrs
written by EnGentech"""


class Student:
    """defining a class for Student"""

    def __init__(self, first_name, last_name, age):
        """initializing variables"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """defining function for checks"""

        if type(attrs) is list:
            val = {}
            for lst in self.__dict__.keys() & attrs:
                val[lst] = self.__dict__[lst]
            return val
        else:
            return self.__dict__
# EnGentech sign
