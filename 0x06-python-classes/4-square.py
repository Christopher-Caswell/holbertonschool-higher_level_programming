#!/usr/bin/python3

"""Module of a Square"""


class Square:
    """Tell me about this Square"""
    def __init__(self, size=0):
        """Making a size with the @property"""
        self.__size = size

    @property
    def size(self):
        """@property acts as a getter, returning from setter"""
        return self.__size

    @size.setter
    def size(self, value):
        """mobilizing the code for setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        """Final declaration of the Square's size"""
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
