#!/usr/bin/python3
"""A program using json and class to
store students profile in a dictionary
written by EnGentech"""

class Student:
    """defining a class named student"""

    def __init__(self, first_name, last_name, age):
        """function for initialization"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """json to dictionalry"""

        js = self.__dict__
        return js
# EnGentech sign
