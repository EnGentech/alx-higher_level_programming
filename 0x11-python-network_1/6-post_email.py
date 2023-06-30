#!/usr/bin/python3
"""
Request with post method
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    mail = argv[2]
    content = requests.post(url, data={'email': mail})
    print(content.text)

# Coded by EnGentech
