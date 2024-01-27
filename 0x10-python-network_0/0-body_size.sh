#!/bin/bash
# This script sends a request to a URL, displays the size of the response body
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
