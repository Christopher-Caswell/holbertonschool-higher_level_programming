#!/usr/bin/python3
"""
Outputs a Rectaangle that inherits Base
Is the basis for the logic that is used by
Square later
"""

from models.base import Base


class Rectangle(Base):
    """Have some class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Opening credits for the hit of the year"""
#       if type(height) is not int:
#           return TypeError("Height needs to be an int")
#       if height < 1:
#           return ValueError("Height needs to be greater than 0")
#       if type(width) is not int:
#           return TypeError("Width needs to be an int")
#       if width < 1:
#           return ValueError("Width needs to be greater than 0")
#       if type(x) is not int:
#           return TypeError("X needs to be an int")
#       if x < 1:
#           return ValueError("X needs to be greater than 0")
#       if type(y) is not int:
#           return TypeError("Y needs to be an int")
#       if y < 1:
#           return ValueError("Y needs to be greater than 0")
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def integer_validator(self, name, value):
        """
        He must be an integer!
        How can you tell?
        He hasn't got errors all over him
        """

        if name is "x" or name is "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name is "width" or name is "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x"""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y"""
        self.integer_validator("y", value)
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """per position posited, print progressively"""
        for a in range(self.__y):
            print()
        """y established as downward printed position"""
        for b in range(self.__height):
            for c in range(self.__x):
                print(" ", end="")
                """x established as forward spaces from side bar"""
            for d in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """alters return such that it kicks certain parameters"""
        return ("[Rectangle] (<{}>) {}/{} - {}/{}".format(
                self.id, self.x, self.y,
                self.width, self.height))

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes"""

        if args is () or args is None:
            for x in kwargs:
                setattr(self, x, kwargs[x])
        else:
            butes = ["id", "width", "height", "x", "y"]
            for x in range(len(args)):
                setattr(self, butes[x], args[x])

    def to_dictionary(self):
        """Thar be dicts afoot"""
#        strings = {}
#        for items in dir(self):
#            w = self.get(items)
#            if (items is "width" or
#                    "height" or "size" or
#                    "id" or "x" or "y"):
#                womp[items] = w
#        return womp
#        keys = ["id","x", "size", "y", "width", "height"]
#        flter =  dict(zip(keys, [self.dict[k] for k in keys]))
#        return flter
        book = dict()
        items = ["id", "width", "height", "x","y"]
        for s in items:
            book[s] = getattr(self, s)
        return book
