#!/usr/bin/python3
"""
This code uses a try except error catch
to avoid a program crash when an error arises
from HTTP.
"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        url = argv[1]
        with request.urlopen(url) as response:
            content = response.read().decode("utf-8")
            print(content)
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))

# Coded by EnGentech
