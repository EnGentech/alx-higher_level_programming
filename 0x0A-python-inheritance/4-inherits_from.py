#!/usr/bin/python3
"""A program to check for inheritance
of a class written by EnGentech"""


def inherits_from(obj, a_class):
    """defining a function to check
    for inherited class only"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
# EnGentech sign
