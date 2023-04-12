#!/usr/bin/python3
"""A program to append the content of an
existing text content written by EnGentech"""


def append_write(filename="", text=""):
    """Appending a file content"""

    with open(filename, mode="a", encoding="utf-8") as appen:
        ap = appen.append(text)
        return ap
# EnGentech
