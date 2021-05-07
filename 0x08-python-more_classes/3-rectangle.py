#!/usr/bin/python3
"""
Write a class "Rectangle"
+ pvt att width
+ pvt att height
"""


class Rectangle:
    """
    A class definition of a rectangle
    Stick around. Next we're doing triangles
    """

    def __init__(self, width=0, height=0):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.height = height
        self.width = width

    @property
    def height(self):
        """Returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """"Sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """defines the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Returns a printable version of rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        z = ""
        for x in range(self.height):
            for y in range(self.width):
                z += "#"
            z += chr(10)
        # z += chr(10)
        return z
