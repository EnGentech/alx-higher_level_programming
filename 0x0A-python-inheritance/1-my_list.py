#!/usr/bin/python3
"""A program to inherit a class
written by EnGentech"""


class MyList(list):
    """defining a class MyList"""

    def print_sorted(self):
        """defining function for
        printing sorted replica of list"""
        NewList = self[:]
        NewList.sort()
        print(NewList)
