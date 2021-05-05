#!/usr/bin/python3
import math
"""This is a bytecode replication puzzle"""

class MagicClass():
    """A circle, mathematically"""

    def __init__(self, radius=0):
        """what is the radius of our circle"""
        self.radius = 0
        """initiated lines 0-6"""
        if type(radius) is not int and type(radius) is not float:
            """9 - 42"""
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """radius squared times pi, intuitively"""
        return((self.radius ** 2) * math.pi)

    def circumference(self):
        """radius times pi times 2, intuitively"""
        return((2 * math.pi * self.radius))
