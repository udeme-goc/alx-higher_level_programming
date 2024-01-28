#!/usr/bin/python3
"""
Fetches the status of https://alx-intranet.hbtn.io.

Uses the requests package to send a GET request to the URL and
display the body of the response.
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
