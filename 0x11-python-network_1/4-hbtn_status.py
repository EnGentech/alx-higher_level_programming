#!/usr/bin/python3
"""
The use of requests.get to obtain info
from the internet
"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    content = requests.get(url)
    clas = content.text.__class__
    txt = content.text

    print("Body response:\n\t- type: {}\n\t- content: {}".format(clas, txt))
    print(content.status_code)

# Coded by EnGentech
