#!/usr/bin/python3
"""
Create a locked class
wherein the only malleable
variable is first_name
"""


class LockedClass():
    """A class for the class of it"""
    __slots = ["first.name"]

    def __init__(self, first_name):
        """oof"""
        self.first.name = first_name
