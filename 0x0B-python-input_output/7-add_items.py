#!/usr/bin/python3
"""A program to load, add and save using
json approach sub written by EnGentech"""

from os import path
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


lst = []
if path.exists("add_item.json"):
    lst = load_from_json_file("add_item.json")
lst = lst + argv[1:]
save_to_json_file(lst, "add_item.json")
# EnGentech
