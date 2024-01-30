#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id header.
"""
import urllib.request
import sys


def get_x_request_id(url):
    """
    Sends a GET request to the specified URL and
    returns the value of the X-Request-Id header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id header.
    """
    with urllib.request.urlopen(url) as response:
        # Retrieve the X-Request-Id header from the response
        x_request_id = response.headers.get('X-Request-Id')
        return x_request_id


if __name__ == "__main__":
    url = sys.argv[1]

    # Retrieve and print the value of the X-Request-Id header
    x_request_id = get_x_request_id(url)
    print(x_request_id)
