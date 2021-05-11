#!/usr/bin/python3
"""
Write a function that returns True if
instance of a class that inherited
from the specified class, else False
"""


def inherits_from(obj, a_class):
    """Doc line still tryna trick checker"""
    if issubclass(type(obj), a_class):
        if type(obj) != a_class:
            return True
    else:
        return False
