#!/usr/bin/python3

"""
Write a function that returns True if
instance of a class that inherited
from the specified class, else False
"""


def inherits_from(obj, a_class):
    """
    I will likely spend all of tomorrow
    trying to find a simpler way to do this
    """
    if issubclass(type(obj), a_class):
        if type(obj) != a_class:
            return True
    else:
        return False
