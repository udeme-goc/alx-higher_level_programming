# 0x11. Python - Network #1

## Overview
This repository contains a collection of Python scripts focused on network programming, specifically dealing with HTTP requests, responses, and interactions with web APIs. These scripts are designed to demonstrate various aspects of network programming using Python, including making requests, handling responses, error handling, and more.

## Table of Contents
1. [Requirements](#requirements)
2. [File Descriptions](#file-descriptions)
3. [Usage](#usage)
4. [Author](#author)
5. [GitHub Repository](#github-repository)

## Requirements
- Python 3.8.5
- Ubuntu 20.04 LTS
- pycodestyle 2.8.* (for PEP 8 compliance)
- requests package

## File Descriptions
- `0-hbtn_status.py`: Fetches the status of https://alx-intranet.hbtn.io using the `urllib` package.
- `1-hbtn_header.py`: Takes a URL as input, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the response header, using the `urllib` package.
- `2-post_email.py`: Takes a URL and an email address as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response, using the `urllib` package.
- `3-error_code.py`: Takes a URL as input, sends a request to the URL, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints the error code, using the `urllib` package.
- `4-hbtn_status.py`: Fetches the status of https://alx-intranet.hbtn.io using the `requests` package.
- `5-hbtn_header.py`: Takes a URL as input, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the response header, using the `requests` package.
- `6-post_email.py`: Takes a URL and an email address as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response, using the `requests` package.
- `7-error_code.py`: Takes a URL as input, sends a request to the URL, and displays the body of the response. If an HTTP error occurs, it prints the error code, using the `requests` package.

## Usage
Each script can be executed from the command line with appropriate arguments. See the header of each script file for usage details.

Example:
```bash
./0-hbtn_status.py
```

## Author
[Udeme Harrison](https://github.com/udeme-goc)

## GitHub Repository
[GitHub - udeme-goc/0x11-python-network_1](https://github.com/udeme-goc/0x11-python-network_1)
