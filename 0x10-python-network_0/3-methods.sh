#!/bin/bash
# Display the content of the web
curl -sI <URL> | awk '/^Allow:/ {print substr($0, 8)}'
