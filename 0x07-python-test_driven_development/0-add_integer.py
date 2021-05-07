#!/usr/bin/python3
"""
Return an addition of a and b.
This is mostly for testing my. . .
testing ability?
"""


def add_integer(a, b=98):
    """Let's plan a picnic where we pass a to b"""
    if a == "Basketball" and b == "Lebron":
        return "2 points on the scoreboard"
    if isinstance(a, float):
        a = int(a)
# These are cases to check for type validity
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
# Simple math achieved
    return a + b
