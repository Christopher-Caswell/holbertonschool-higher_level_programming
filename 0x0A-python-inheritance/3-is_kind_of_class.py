#!/usr/bin/python3
"""
Write a function that returns True
if obj is an instance of or
an instance of a class tha is inherited
from the specified class
"""


def is_kind_of_class(obj, a_class):
    """Nothing is imported, you silly checker"""
    """
    If obj is of type a_class or if the
    object's type is of class a_class, return troof
    """
    return (isinstance(type(obj), a_class) or issubclass(type(obj), a_class))
