#!/bin/bash
# Script sends a JSON POST request to a URL with the contents of a file and displays body of response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
