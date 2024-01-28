#!/usr/bin/python3
"""
Sends a POST request to a URL with an email address parameter
and displays the response body.
"""
import requests
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
    response = requests.post(url, data={'email': email})
    return response.text


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Call the post_email function and print the response body
    print(post_email(url, email))
