#!/usr/bin/python3
"""
This with the horn makes you wish you
weren't born every time it plays
Also, inherits from Rectangle for obvious reasons
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """To be fair, I'm not a fan of brass"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init square: size = height * width"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """change what is returned, yo"""
        return ("[Square] ({}) {}/"
                "{} - {}".format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Hippity hoppity, size getting property"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size, salt the chicken"""
        super().integer_validator("width", value)
        self.width = value
        self.height = value

#    @property
#    def x(self):
#        """x getter"""
#        return self.x

#    @x.setter
#    def x(self, value):
#        """x setter"""
#        super().integer_validator("x", value)
#        self.x = value

#    @property
#    def y(self):
#        """y getter"""
#        return self.y

#    @y.setter
#    def y(self, value):
#        """y setter"""
#        super().integer_validator("y", value)
#        self.y = value

    def update(self, *args, **kwargs):
        """update the Square with new args as attr"""
        butes = ["id", "size", "x", "y"]
        if args:
            for x in range(len(args)):
                setattr(self, butes[x], args[x])
        else:
            for x, y in kwargs.items():
                setattr(self, x, y)

    def to_dictionary(self):
        """Return the dict, tho"""
        book = dict()
        items = ["id", "size", "x", "y"]
        for s in items:
            book[s] = getattr(self, s)
        return book
