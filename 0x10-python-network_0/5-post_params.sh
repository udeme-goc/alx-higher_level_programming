#!/bin/bash
# Send POST request using curl with parameters and display body of response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
