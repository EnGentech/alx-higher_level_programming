#!/usr/bin/python3
"""A program to echo users name pending on input
and to check is the input entered by user is a string type"""


def say_my_name(first_name="", last_name=""):
    """say me name write your name to the standard output"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
# EnGentech signature
