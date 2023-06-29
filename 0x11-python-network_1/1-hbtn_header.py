#!/usr/bin/python3
"""Display the Id of the site provided
in the argv system library
"""
import urllib.request
import sys

if __name__ == "__main__":
    get_val = 'X-Request-Id'
    url = sys.argv[1]
    with urllib.request.urlopen(url) as file:
        con = file.headers.get(get_val)

    print(con)

# Coded by EnGentech
