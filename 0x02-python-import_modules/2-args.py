#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("0 arguments.")
else:
    num_args = len(sys.argv) - 1
    plural = "s" if num_args > 1 else ""
    print("{} argument{}:".format(num_args, plural))

    for i in range(1, num_args + 1):
        print("{}: {}".format(i, sys.argv[i]))
