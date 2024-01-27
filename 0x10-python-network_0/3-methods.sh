#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send OPTIONS request using curl to retrieve supported methods
METHODS=$(curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d' '-f2-)

# Display supported methods
echo "$METHODS"
