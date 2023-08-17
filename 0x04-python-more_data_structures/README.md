# 0x04. Python - More Data Structures: Set, Dictionary

## Description

This repository contains Python scripts that demonstrate the usage of sets and dictionaries, two important data structures in Python. The scripts cover various operations and manipulations you can perform with sets and dictionaries, helping you understand their functionalities better.

## Table of Contents

- [Project Title](#0x04-python---more-data-structures-set-dictionary)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Files and Directories](#files-and-directories)
  - [Usage](#usage)
  - [Author](#author)
  - [License](#license)

## Files and Directories

- `0-square_matrix_simple.py`: A Python script that computes the square value of all integers of a matrix.
- `1-search_replace.py`: A Python script that replaces all occurrences of an element by another in a new list.
- `2-uniq_add.py`: A Python script that adds all unique integers in a list.
- `3-common_elements.py`: A Python script that returns a set of common elements in two sets.
- `4-only_diff_elements.py`: A Python script that returns a set of all elements present in only one set.
- `5-number_keys.py`: A Python script that returns the number of keys in a dictionary.
- `6-print_sorted_dictionary.py`: A Python script that prints a dictionary by ordered keys.
- `7-update_dictionary.py`: A Python script that replaces or adds key/value in a dictionary.
- `8-simple_delete.py`: A Python script that deletes a key in a dictionary.
- `9-multiply_by_2.py`: A Python script that returns a new dictionary with all values multiplied by 2.
- `10-best_score.py`: A Python script that returns the key with the biggest integer value in a dictionary.
- `11-multiply_list_map.py`: A Python script that multiplies all values in a list by a given number using map.
- `12-roman_to_int.py`: A Python script that converts a Roman numeral to an integer.
- `100-weight_average.py`: A Python script that computes the weighted average of all integers in a list of tuples.
- `101-square_matrix_map.py`: A Python script that computes the square value of all integers of a matrix using map.
- `102-complex_delete.py`: A Python script that deletes keys with a specific value in a dictionary.
- `103-python.c`: A C file containing functions to print information about Python lists and bytes objects.
- `103-tests.py`: A Python script to test the functions in `103-python.c`.

## Usage

To run any of the Python scripts, execute them using the Python interpreter. For example:

```bash
python3 0-square_matrix_simple.py

For the C functions in 103-python.c, compile the source file into a shared library and use the provided test script:

```bash
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
python3 103-tests.py

## Author
Udeme Harrison
GitHub: udeme-goc

## License
This project is licensed under the MIT License - see the LICENSE file for details.
