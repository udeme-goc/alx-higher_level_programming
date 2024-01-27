#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request using curl and retrieve body size
BODY_SIZE=$(curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}')

# Display the size of the body in bytes
echo "$BODY_SIZE"
