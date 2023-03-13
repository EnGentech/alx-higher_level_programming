#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not my_list:
        return
    else:
        new_lst = [val % 2 == 0 for val in my_list]

    return new_lst
