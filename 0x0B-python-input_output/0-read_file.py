#!/usr/bin/python3
"""A program to read the content of a txt file
written by EnGentech"""


def read_file(filename=""):
    """function to read a file"""

    with open(filename, mode='r', encoding="utf-8") as ReadMe:
        print(ReadMe.read())

# EnGentech
