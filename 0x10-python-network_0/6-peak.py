#!/usr/bin/python3
"""Find the peak of the list provided"""


def find_peak(list_of_integers):
    """A defined function to sort and list"""
    if list_of_integers:
        new_num = sorted(list_of_integers)
        peak = new_num[len(list_of_integers) - 1]
        return (peak)
    else:
        return (None)

# Coded by EnGentech
