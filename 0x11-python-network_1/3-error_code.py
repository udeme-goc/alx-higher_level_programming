#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If an HTTP error occurs, prints the error code.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            # Display the body of the response
            print(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            # If an HTTP error occurs, print the error code
            print("Error code:", e.code)
