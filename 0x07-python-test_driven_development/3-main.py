#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

first_name = "Jon"
last_name = "Doe"
say_my_name(first_name, last_name)
first_name = ""
last_name = "Doe"
say_my_name(first_name, last_name)
first_name = "Jon"
last_name = ""
say_my_name(first_name, last_name)
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
