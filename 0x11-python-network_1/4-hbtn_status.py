#!/usr/bin/python3
"""
The requests module to get HTTP
content over the internet with the
printed pattern as
Body response:$
    - type: <class 'str'>$
    - content: OK$
"""
import requests
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    a = requests.get(url)

    new = a.content.decode('utf-8')
    print("Body response:\n\t- type: {}\n\t- content:\
    {}".format(new.__class__, new))
