#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send GET request using curl and store response body
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ $response -eq 200 ]; then
	curl -s "$1"
fi
