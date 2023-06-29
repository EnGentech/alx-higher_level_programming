#!/usr/bin/python3
"""Get the content from https://alx-intranet.hbtn.io/status
and display in a certain way as seen below
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
"""
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as rqst:
        html = rqst.read()

    utf_content = html.decode('utf-8')
    content = html
    clas = html.__class__
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(clas, content, utf_content))
# Coded by EnGentech
