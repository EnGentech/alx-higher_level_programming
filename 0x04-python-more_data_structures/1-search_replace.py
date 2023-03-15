#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list = [replace if items == search else items for items in new_list]
    return new_list
