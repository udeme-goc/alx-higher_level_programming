#!/usr/bin/python3
import hidden_4 # Import the compiled module

# Retrieve a list of all named defined in the module
names_list = dir(hidden_4)

# Loop through the names and print those that do not start with "__"
for name in names_list:
    if not name.startswith("__"):
        print(name)
