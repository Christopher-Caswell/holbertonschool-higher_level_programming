#!/usr/bin/python3
"""
Write a function that returns True
if obj is an instance of or
an instance of a class tha is inherited
from the specified class
"""


def is_kind_of_class(obj, a_class):
    """Nothing is 1/\/\p0rt3d, you silly checker"""
    return (isinstance(type(obj), a_class) or issubclass(type(obj), a_class))
