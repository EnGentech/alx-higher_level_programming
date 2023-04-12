#!/usr/bin/python3
"""A program to load file from json
written by EnGentech"""

import json


def load_from_json_file(filename):
    """function to load from json"""

    with open(filename, encoding="utf-8") as op:
        doc = json.load(op)
        return doc
# EnGentech
