#!/bin/bash
# Display the content of the web
curl "$1" -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD"
