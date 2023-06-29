#!/usr/bin/python3
"""Get a response message from the server
with a query string passed to the server
basically an email
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email_address = sys.argv[2]
    dat = {'email': email_address}
    data = parse.urlencode(dat).encode('utf-8')
    reqst = request.Request(url, data=data)

    with request.urlopen(reqst) as file:
        mail = file.read().decode('utf-8')

        print(mail)

# Coded by EnGentech
