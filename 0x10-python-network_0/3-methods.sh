#!/bin/bash
# Display the content of the web
curl -sI "$1" | awk '/^Allow:/ {print substr($0, 8)}'
