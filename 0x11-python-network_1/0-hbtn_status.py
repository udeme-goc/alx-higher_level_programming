#!/usr/bin/python3
import urllib.request


def fetch_status(url):
    """
    Fetches the status of a specified URL using urllib.

    Args:
        url (str): The URL to fetch.

    Returns:
        bytes: The content of the response.
    """
    with urllib.request.urlopen(url) as response:
        content = response.read()
        return content


if __name__ == "__main__":
    # Define the URL to fetch
    url = "https://alx-intranet.hbtn.io/status"

    # Fetch the status and print relevant information
    content = fetch_status(url)
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
