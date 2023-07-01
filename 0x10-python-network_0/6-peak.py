#!/usr/bin/python3
"""Find the peak of the list provided"""

def find_peak(list_of_integers):
    if list_of_integers:
        new_num = sorted(list_of_integers)
        peak = new_num[len(num) - 1]
        print(peak)
    else:
        print(None)

find_peak(num)

# Coded by EnGentech
