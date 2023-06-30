#!/usr/bin/python3
"""
Header request
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    content = requests.get(url)

    print(content.headers.get('X-Request-Id'))

# Coded by EnGentech
