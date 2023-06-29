#!/usr/bin/python3
"""
This code uses a try except error catch
to avoid a program crash when an error arises
from HTTP.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            content = response.read().decode("utf-8")
            print(content)
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))

# Coded by EnGentech
