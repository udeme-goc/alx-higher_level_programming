#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send POST request using curl with parameters and display body of response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
