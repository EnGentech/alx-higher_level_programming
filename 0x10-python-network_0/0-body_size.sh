#!/bin/bash
# print the size of the page body using port 5000
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
