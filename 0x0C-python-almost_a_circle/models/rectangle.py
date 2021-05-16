#!/usr/bin/python3
"""
Outputs a Rectaangle that inherits Base
Is the basis for the logic that is used by
Square later
"""


class Rectangle(Base):
    """Have some class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Opening credits for the hit of the year"""
        if type(height) is not int:
            return TypeError("Height needs to be an int")
        if height is < 1:
            return ValueError("Height needs to be greater than 0")
        if type(width) is not int:
            return TypeError("Width needs to be an int")
        if width is < 1:
            return ValueError("Width needs to be greater than 0")
        super().__init__(id)
        self.__height = height
        self.__width = width
        self.x = x
        self.y = y

    def integer_validator(self, name, value):
        """
        He must be an integer!
        How can you tell?
        He hasn't got errors all over him
        """

        if name is "x" or "y":
            if value < 0:
                raise ValueError("{:s} must be >= 0".format(name))
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if name is not "x" or "y" and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        self.integer_validator("height", height)
        self.__height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        self.integer_validator("width", width)
        self.__width = width

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x"""
        self.integer_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y"""
        self.integer_validator("y", y)
        self.__y = y

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """per position posited, print progressively"""
        for a in range(self.__y):
            print()
        """y established as downward printed position"""
        for b in range(self.__height):
            for c in len(self.__x):
                print(" ", end="")
                """x established as forward spaces from side bar"""
            for d in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return ("[Rectangle] (<{:d}>) {:d}/{:d} - {}/{}".format(
                self.__id, self.__x, self.__y,
                self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes"""

        if args is () or args is None:
            for x in kwargs:
                setattr(self, key, kwargs[x])
        else:
            butes = ["id", "width", "height", "x", "y"]
            for x in range(len(kwargs)):
                setattr(self, butes[x], args[x])

    def to_dictionary(self):
        """Thar be dicts afoot"""
        return dir(self)
