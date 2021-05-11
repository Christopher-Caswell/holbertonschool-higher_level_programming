#!/usr/bin/python3
"""
Write a subclass Rectangle
that inherits BaseGeometry
And defrines wid and hei
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
