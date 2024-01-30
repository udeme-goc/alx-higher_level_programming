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
    try:
        response = requests.get(url)
        response.raise_for_status()     # Raise HTTPError fir bad status codes
        return response
    except requests.exceptions.HTTPError as e:
        return e


if __name__ == "__main__":
    url = sys.argv[1]
    response = get_response(url)

    if isinstance(response, requests.exceptions.HTTPError):
        # If an HTTP error occurs, print the error code
        print("Error code:", response.response.status_code)
    else:
        # Display the body of the response
        print(response.text)
