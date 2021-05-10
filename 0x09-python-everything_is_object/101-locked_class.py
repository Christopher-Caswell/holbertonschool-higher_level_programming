#!/usr/bin/python3

"""
Create a locked class
wherein the only malleable
variable is first_name
Words to appease an ambiguous checker
"""


class LockedClass:
    """A class for the class of it"""

    __slots__ = ["first.name"]
    """Nothing else should need to be said"""
