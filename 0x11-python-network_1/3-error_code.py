#!/usr/bin/python3
"""
A program to access the internet, get content
and check for possible error that may arise
using HTTPerror checks
"""
from urllib import request, error
from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
        with request.urlopen(url) as response:
            content = response.read()
            print(content)
    except error.HTTPError as ero:
        print("Error code: {}".format(ero.code))
        
# Coded by EnGentech
