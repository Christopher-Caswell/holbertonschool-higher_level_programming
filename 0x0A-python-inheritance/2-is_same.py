#!/usr/bin/python3

"""
Write a function that returns
True if object is exactly an instance
of the specified class
"""


def is_same_class(obj, a_class):
    return isinstance(type(obj), a_class)
