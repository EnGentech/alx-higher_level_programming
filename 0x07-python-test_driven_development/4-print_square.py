#!/usr/bin/python3
"""A program to print '#' at
size times depending on user
writen by EnGentech"""


def print_square(size):
    """A program to print the string '#'
    pending the size inputed by the user"""
    if type(size) is not int:
        raise TypeError("size must be integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
# EnGentech signature
