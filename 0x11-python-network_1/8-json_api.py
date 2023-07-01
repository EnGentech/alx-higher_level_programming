#!/usr/bin/python3
"""
Header request
"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        var = ""
        if len(argv) > 1:
            var = argv[1]

        url = 'http://0.0.0.0:5000/search_user'
        data = {'q': var}

        reply = requests.post(url, data=data)
        obtain = reply.json()

        if obtain == {}:
            print("No result")
        else:
            print("[{}] {}".format(obtain['id'], obtain['name']))
    except ValueError:
        print('Not a valid JSON')

# Coded by EnGentech
