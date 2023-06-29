#!/usr/bin/python3
"""Get a response message from the server
with a query string passed to the server
basically an email
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    get_val = 'X-Request-Id'
    url = sys.argv[1]
    email_address = sys.argv[2]
    data = {'email': email_address}
    data = parse.urlencode(data).encode('utf-8')
    reqst = request.Request(url, data=data)

    with request.urlopen(reqst) as file:
        mail = file.read()

    print("Your email is: {}".format(mail))

# Coded by EnGentech
