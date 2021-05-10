#!/usr/bin/python3
"""
Create a locked class
wherein the only malleable
attribute is first_name
"""


class LockedClass():
    """A class for the class of it"""
    __slots__ = 'first_name',
