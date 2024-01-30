#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
"""

import requests
import sys


def search_user(letter):
    """
    Sends POST request to search_user endpoint with given letter as parameter.

    Args:
        letter (str): The letter to search for.

    Returns:
        str: The response from the server.
    """
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(url, data=data)
    return response.json()


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ''
    response = search_user(letter)

    if response:
        if isinstance(response, dict):
            if 'id' in response and 'name' in response:
                print("[{}] {}".format(response['id'], response['name']))
            else:
                print("No result")
        else:
            print("Not a valid JSON")
    else:
        print("No result")
