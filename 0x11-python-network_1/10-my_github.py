#!/usr/bin/python3
"""The python API using github interface"""

import requests
from sys import argv

if __name__ == '__main__':
    try:
        username = argv[1]
        token = argv[2]

        url = 'http://api.github.com/users/{}'.format(username)
        header = {
            'Authorization': 'token {}'.format(token)
        }

        content = requests.get(url, headers=header).json()
        print(content["id"])
    except KeyError:
        print("None")

# Coded by EnGentech
