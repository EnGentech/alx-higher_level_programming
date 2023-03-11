#!/usr/bin/python3
def element_at(my_list, idx):
    for li in my_list:
        if idx % 2 == 0 and idx < len(my_list):
            return my_list[idx]
        else:
            return None
