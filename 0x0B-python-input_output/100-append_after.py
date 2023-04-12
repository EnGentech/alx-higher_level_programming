#!/usr/bin/python3
"""A program to append a string base
on search value written by EnGentech"""


def append_after(filename="", search_string="", new_string=""):
    """function to append file base on string"""

    with open(filename, mode="r", encoding="utf-8") as rd:
        rd_line = rd.readline()

    with open(filename, mode="w", encoding="utf-8") as rd:
        for i in rd_line:
            rd.write(i)
            if search_string in i:
                rd.write(new_string)
# EnGentech sign
