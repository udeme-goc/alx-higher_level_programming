#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics based on a specific log format.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
it prints those statistics since the beginning:
- Total file size: File size: <total size> (sum of all previous sizes)
- Number of lines by status code (sorted in ascending order).

Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500.

Author: Udeme Harrison
"""

import sys


def print_metrics(total_size, status_counts):
    """
    Print the metrics based on the provided data.

    Args:
        total_size (int): The total file size.
        status_counts (dict):
            A dictionary containing counts of different status codes.
    """
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(status_code, count))


def parse_log_line(line, status_counts):
    """
    Parse a log line and update metrics.

    Args:
        line (str): A log line to be parsed.
        status_counts (dict):
            A dictionary containing counts of different status codes.
    """
    try:
        # Split the log line into words.
        data = line.split()
        if len(data) > 2:
            # Extract the status code (second to last element).
            status_code = data[-2]
            if status_code in status_counts:
                status_counts[status_code] += 1
            # Extract file size (last element) and convert it to an integer.
            size = int(data[-1])
            return size
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    # Initialize variables to track total size and status code counts.
    total_size = 0
    status_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    try:
        line_count = 0
        for line in sys.stdin:
            # Parse the log line and get the file size.
            size = parse_log_line(line, status_counts)
            # Update the total size.
            total_size += size
            line_count += 1
            if line_count % 10 == 0:
                # Print metrics every 10 lines.
                print_metrics(total_size, status_counts)
    except KeyboardInterrupt:
        # Handle keyboard interruption and print metrics.
        print_metrics(total_size, status_counts)
        raise
