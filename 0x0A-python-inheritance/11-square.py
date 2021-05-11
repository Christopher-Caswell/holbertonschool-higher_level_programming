#!/usr/bin/python3
"""
Write a class BaseGeometry
public instance method: def area(self):
raise an exception when area() is not implemented
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Bourgeoisie geometry"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Hipness is calculated thusly: 2(b**2)"""
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
