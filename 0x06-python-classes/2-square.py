#!/usr/bin/python3

"""Module, bro. Module. This module defines a private square."""


class Square:
    """Show me the private Square"""
    def __init__(self, size=0):
        """A protection before the computation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """The actual calculation"""
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                """Lastly, declare the value to define the square"""
                self.__size = size
