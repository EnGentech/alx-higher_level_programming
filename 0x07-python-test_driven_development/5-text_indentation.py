#!/usr/bin/python3
"""A program to print two new
lines with . ? and : are found
in a string writen by EnGentech with
support from Rhomieniel"""


def text_indentation(text):
    """code to print string inputed by user
    with special conditions"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
    # EnGentech no_signature
