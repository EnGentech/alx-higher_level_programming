#!/usr/bin/python3
"""A program to count the number
of string in a file written by
EnGentech"""


def write_file(filename="", text=""):
    """A function to count text length"""

    with open(filename, mode="w", encoding="utf-8") as Count:
        num = 0
        num = Count.write(text)
        return num
# EnGentech sign
