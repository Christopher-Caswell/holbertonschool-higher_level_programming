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
    number_of_instances is a public class attribute
    print_symbol is an attribute that takes any argument
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
        """A printable output of the rectangle"""
        z = ""
        if self.height == 0 or self.width == 0:
            return ""
        for x in range(self.height):
            for y in range(self.width):
                z += str(self.print_symbol)
            if x != self.height - 1:
                z += chr(10)
        return z

    def __repr__(self):
        """The rectangle outputs a string of itself"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletion method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """To compare Rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() >= rect_1.area():
            return rect_2
        else:
            return rect_1
