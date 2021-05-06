#!/usr/bin/python3
"""
Print a first and last name from input
first and last names must be strings
Last name will return as empty input
"""

def say_my_name(first_name, last_name=""):
    """Step one: make the func"""
    if not isinstance(first_name, str):
        return TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        return TypeError("last_name must be a string")
        """Can't stop the func"""

    print("My name is {} {}".format(first_name, last_name))
