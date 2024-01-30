#!/usr/bin/python3
"""
Uses the GitHub API to display the user id.
"""

import requests
import sys


def get_user_id(username, token):
    """
    Retrieves the user id using the GitHub API.

    Args:
        username (str): The GitHub username.
        token (str): The personal access token.

    Returns:
        str: The user id, or None if authentication fails.
    """
    # Construct the URL for the GitHub API endpoint for the specified username
    url = f"https://api.github.com/users/{username}"

    # Set up headers for the request with Basic Authentication using the PAT
    headers = {"Authorization": f"token {token}"}

    # Send a GET request to the GitHub API endpoint
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the user id
        return response.json()["id"]
    else:
        # If authentication fails or user not found, return None
        return None


if __name__ == "__main__":
    # Get the GitHub username and PAT from command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # Call the get_user_id function to retrieve the user id
    user_id = get_user_id(username, token)

    # Print the user id or "None" if authentication fails
    print(user_id if user_id else "None")
