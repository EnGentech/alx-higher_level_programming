#!/usr/bin/bash
# print the size of the page body using port 5000
curl -sI GET $1 | head -n5 | tail -n1 | awk '{print $2}'
