#!/usr/bin/python3
"""A program to dump a file using json
into an object written by EnGentech"""

import json


def save_to_json_file(my_obj, filename):
    """function to define my_obj throgh json"""

    with open(filename, mode='w', encoding="utf-8") as file:
        myfile = json.dump(my_obj, file)
        return myfile
# EnGentech
