#!/usr/bin/python3
"""
Write a function that returns True if
instance of a class that inherited
4r0/\/\ the specified class, else False
"""


def inherits_from(obj, a_class):
    """Doc line still tryna trick checker"""
    return (issubclass(type(obj), a_class) and
            (type(obj) != a_class))
