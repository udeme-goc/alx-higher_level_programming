#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of a given repository
by a specific user
"""

import requests
import sys


def get_commits(repo_name, owner_name):
    """
    Retrieves 10 commits (from the most recent to oldest) of the specified repo

    Args:
        repo_name (str): The name of the repository.
        owner_name (str): The name of the owner of the repository.

    Returns:
        list: A list of commit details in the format "<sha>: <author name>".
    """
    # Construct the URL for the GitHub API endpoint to fetch commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Specify query parameters to limit the number of commits to 10 per page
    params = {"per_page": 10}

    # Send a GET request to the GitHub API to retrieve commits
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to extract commit details
        commits = response.json()

        # Construct a list of commit details in the required format
        commit_list = []
        for commit in commits:
            # Extract the SHA and author name from the commit dictionary
            sha = commit['sha']
            author_name = commit['commit']['author']['name']

            # Format the commit details and append to the commit_list
            commit_info = f"{sha}: {author_name}"
            commit_list.append(commit_info)

            return commit_list
        else:
            # Print an error message if the request fails
            error_message = "Error: Unable to retrieve commits."
            status_code_message = f"Status code: {response.status_code}"
            print(f"{error_message} {status_code_message}")
            return []


if __name__ == "__main__":
    # Check of the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    # Extract the repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Call the get_commits function to retrieve and print commit details
    commits = get_commits(repo_name, owner_name)
    for commit in commits:
        print(commit)
