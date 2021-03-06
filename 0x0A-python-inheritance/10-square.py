#!/usr/bin/python3
"""
Write a square that pulls form Rectangle
and outputs measurements of the square
also, this line exists
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Bourgeoisie geometry"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Hipness is calculated thusly: 2(b**2)"""
        return (self.__size * self.__size)
