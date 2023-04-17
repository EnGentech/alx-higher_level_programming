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

    @classmethod
    def save_to_file(cls, list_objs):
        """function to save file using json"""

        file_out = cls.__name__ + ".json"
        if list_objs is None:
            file_object = []
        else:
            file_object = [obj.to_dictionary() for obj in list_objs]
        with open(file_out, mode="w", encoding="utf-8") as file_open:
            file_open.write(cls.to_json_string(file_object))

# EnGentech sign
