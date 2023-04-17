#!/usr/bin/python3

import json

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

    def to_json_string(list_dictionaries):
        """a funtion to dump into json"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

# EnGentech sign
