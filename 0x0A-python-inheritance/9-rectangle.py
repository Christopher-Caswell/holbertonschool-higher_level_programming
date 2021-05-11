#!/usr/bin/python3
"""
Write a class BaseGeometry
public instance method: def area(self):
raise an exception when area() is not implemented
"""


class BaseGeometry:
    """Come and see the shapes inherent in the system"""
    """Help! Help! I'm being addressed!"""

    def integer_validator(self, name, value):
        """
        He must be an integer!
        How can you tell?
        He hasn't got errors all over him
        """
        if name is not type(str):
            pass
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


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

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        """She's got great tracts of land"""
        return (self.__height * self.__width)
