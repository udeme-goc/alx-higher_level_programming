# 0x0A. Python - Inheritance

## Description

This repository contains Python scripts that demonstrate concepts related to inheritance.

## Files

- `0-lookup.py`: Python script that returns the list of available attributes and methods of an object.
- `1-my_list.py`: Python script that defines a class `MyList` that inherits from `list`. It contains a method `print_sorted` that prints the list sorted in ascending order.
- `2-is_same_class.py`: Python script that defines a function `is_same_class` which returns `True` if an object is exactly an instance of a specified class, otherwise `False`.
- `3-is_kind_of_class.py`: Python script that defines a function `is_kind_of_class` which returns `True` if an object is an instance of a specified class or a class that inherited from it, otherwise `False`.
- `4-inherits_from.py`: Python script that defines a function `inherits_from` which returns `True` if an object is an instance of a class that inherited from a specified class, otherwise `False`.
- `5-base_geometry.py`: Python script that defines an empty class `BaseGeometry`.
- `6-base_geometry.py`: Python script that defines class `BaseGeometry` with a method `area` that raises an Exception with the message `area() is not implemented`.
- `7-base_geometry.py`: Python script that defines class `BaseGeometry` with methods `area` and `integer_validator`.
- `8-rectangle.py`: Python script that defines class `Rectangle` which inherits from `BaseGeometry`.
- `9-rectangle.py`: Python script that defines class `Rectangle` which inherits from `BaseGeometry` and overrides the `__str__` method.
- `10-square.py`: Python script that defines class `Square` which inherits from `Rectangle`.
- `11-square.py`: Python script that defines class `Square` which inherits from `Rectangle` and overrides the `__str__` method.
- `100-my_int.py`: Python script that defines class `MyInt` which inherits from `int` and overrides the equality operators.
- `101-add_attribute.py`: Python script that defines a function `add_attribute` which adds a new attribute to an object if possible.

## Usage

Each Python script can be run separately and contains docstring comments for further details. For example:

```bash
$ ./0-lookup.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

## Author

[Udeme Harrison](https://github.com/udeme-goc)

## Acknowledgements

This project is part of the curriculum at [ALX](https://alx-intranet.hbtn.io/). Special thanks to all the staff and peers.