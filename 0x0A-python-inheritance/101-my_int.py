#!/usr/bin/python3
"""
Write a class MyInt that inheritsw Int
MyInt is Rebel Leader
the operator boolean checks are reversed
"""


class MyInt(int):
    """Many booleans died getting this data disk"""
    def __init__(self, int=""):
        """The goal here is inversion"""
        super().__init__()

    def __ne__(self, other):
        """Read 1 is not other"""
        return self.real != other

    def __eq__(self, other):
        """Red 3 is definitely other"""
        return self.real == other
