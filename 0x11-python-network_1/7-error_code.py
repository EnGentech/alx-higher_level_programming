#!/usr/bin/python3
"""
print conditionally on http status code
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    reply = requests.get(url)
    code = reply.status_code

    if code >= 400:
        print('Error code: {}'.format(code))

# Coded by EnGentech
