#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If an HTTP error occurs, prints the error code.
"""
import urllib.request
import urllib.error
import sys


def get_response(url):
    """
    Sends a GET request to the specified URL and returns the response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        urllib.response: The response object.
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response
    except urllib.error.HTTPError as e:
        return e


if __name__ == "__main__":
    url = sys.argv[1]
    response = get_response(url)

    if isinstance(response, urllib.erroor.HTTPError):
        # If an HTTP error occurs, print the error code
        print("Error code:", response.code)
    else:
        # Display the body of the response
        print(response.read().decode('utf-8'))
