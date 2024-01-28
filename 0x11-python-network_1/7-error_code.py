#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If an HTTP error occurs, prints the error code.
"""
import requests
import sys


def get_response(url):
    """
    Sends a GET request to the specified URL and returns the response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        requests.Response: The response object.
    """
    return requests.get(url)


if __name__ == "__main__":
    url = sys.argv[1]
    response = get_response(url)

    print(response.text)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
