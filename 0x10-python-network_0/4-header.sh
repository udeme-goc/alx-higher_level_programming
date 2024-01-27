#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send GET request using curl with custom header and display body of response
curl -sH "X-School-User-Id: 98" "$1"
