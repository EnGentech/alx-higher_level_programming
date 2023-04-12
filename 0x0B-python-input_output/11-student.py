#!/usr/bin/python3
"""A program to reload attributes by
loading a json file written by EnGentech"""


class Student:
    """defining class for student"""

    def __init__(self, first_name, last_name, age):
        """initializing stage"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function to check for list items"""

        if type(attrs) is list:
            val = {}
            for lst in self.__dict__.keys() & attrs:
                val[lst] = self.__dict__[lst]
            return val
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """function to reload attribute"""

        for key, value in json.items():
            self.__setattr__(key, value)
# EnGentech sign
