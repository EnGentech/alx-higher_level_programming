#!/usr/bin/python3
"""A program to load file content
using json written by EnGentech"""

import json


def from_json_string(my_str):
    """a function defining json load"""

    rf_json = json.loads(my_str)
    return rf_json
# EnGentech sign
