#!/usr/bin/python3
"""
print conditionally on http status code
"""
import requests

if __name__ == "__main__":
    reply = requests.get('http://engentech.tech/com')
    code = reply.status_code

    if code >= 400:
        print('Error code: {}'.format(code))

# Coded by EnGentech
