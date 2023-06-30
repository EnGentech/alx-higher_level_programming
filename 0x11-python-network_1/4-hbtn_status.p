#!/usr/bin/python3
"""
The use of requests.get to obtain info
from the internet
"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    cont = requests.get(url)
    clas = cont.text.__class__
    txt = cont.text

    print("Body response:\n\t- type: {}\n\t- content: {}".format(clas, txt))

# Coded by EnGentech
