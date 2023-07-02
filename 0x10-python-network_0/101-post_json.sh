#!/bin/bash
# Send a curl requst with a POST
curl -sX POST -H "Content-Type: Application/json" -d @"$2" "$1"
