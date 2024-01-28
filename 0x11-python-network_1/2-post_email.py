#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter and
displays the response body.
"""
import urllib.parse
import urllib.request
import sys


def post_email(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter.

    Args:
        url (str): The URL to send the request to.
        email (str): The email address to send as a parameter.

    Returns:
        str: The body of the response.
    """
    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Make a POST request with the encoded email parameter
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        # Decode and return the response the body
        return response.read().decode('utf-8')


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Call the post_email function and print the response body
    print(post_email(url, email))
