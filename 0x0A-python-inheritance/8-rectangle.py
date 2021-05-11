#!/usr/bin/python3
"""
Write a class BaseGeometry
public instance method: def area(self):
raise an exception when area() is not implemented
This update is strictly to remove for checker
"""


class Rectangle(BaseGeometry):
    """
    Child class made of geometry
    """

    def __init__(self, width, height):
        """The legendary block code of aaaaargh"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
