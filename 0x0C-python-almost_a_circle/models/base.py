#!/usr/bin/python3
"""A program to create a class Base
written by EnGentech"""


class Base:
    """creating a class of base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializing self"""

    if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.if = Base.__nb_objects

# EnGentech sign
