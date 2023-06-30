#!/usr/bin/python3
"""
The use of requests.get to obtain content
from the internet
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'
content = requests.get(url)
clas = content.text.__class__
txt = content.text

print("Body response:\n\t- type: {}\n\t- content: {}".format(clas, txt))

# Coded by EnGentech
