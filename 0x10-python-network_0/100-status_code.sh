#!/bin/bash
# A curl code to return http status code
curl -so /dev/null -w "%{http_code}" "$1"
