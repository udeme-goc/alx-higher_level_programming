#!/usr/bin/python3
import sys

# Initialize a variable to store the sum of arguments
total_sum = 0

# Loop through each arugument starting from index 1 (index 0 contains the scriot name)
for i in range(1, len(sys.argv)):
    # Convert the argument to an integer and add it to the total_sum
    total_sum += int(sys.argv[i])

# Print the total_sum
print(total_sum)
