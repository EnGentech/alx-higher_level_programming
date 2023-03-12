#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        mx = 0
        for chk in range(len(my_lits)):
            if my_list[chk] > mx:
                mx = my_list[chk]

        return mx
