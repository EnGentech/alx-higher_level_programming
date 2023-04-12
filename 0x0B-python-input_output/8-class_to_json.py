#!/usr/bin/python3
"""A program that returns the dictionary description
with simple data structure care of EnGentech"""


def class_to_json(obj):
    """defining function"""

    des = obj.__dict__
    return des
# EnGentech
