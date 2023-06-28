#!/usr/bin/bash
# print the size of the page body using port 5000

curl -so /dev/null -w '%{size_download}\n' $1
