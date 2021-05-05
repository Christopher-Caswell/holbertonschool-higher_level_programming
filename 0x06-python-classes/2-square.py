#!/usr/bin/python3
"""Module defines a private Square."""


class Square:
    """Show me a private square"""

    def ___init__(self, size=0):
        """Defines the square to be of size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
