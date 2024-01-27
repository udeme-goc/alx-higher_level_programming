#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Execute curl in a subshell and capture the output
output=$(curl -s -o /dev/null -w "%{http_code}" "$1"

# Display the status code
echo "$output"
