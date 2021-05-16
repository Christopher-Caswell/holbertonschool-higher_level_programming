#!/usr/bin/python3
"""
This with the horn makes you wish you
weren't born every time it plays
Also, inherits from Rectangle for obvious reasons
"""


class Square(Rectangle):
    """To be fair, I'm not a fan of brass"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init square: size = height * width"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """change what is returned, yo"""
        return ("[Square] ({}) {}/"
                "{} - {}".format(self.id, self.x, self.y, self.size))

    @property
    def size(self, value):
        """Hippity hoppity, size getting property"""
        return self.size

    @size.setter
    def size(self, value):
        """set the size, salt the chicken"""
        super().integer_validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the Square with new args as attr"""
        if args is () or args is None:
            for x in args:
                setattr(self, key, kwargs[x])
        else:
            butes = ["id", "size", "x", "y"]
            for x in range(len(args)):
                setattr(self, butes[x], args[x])

    def to_dictionary(self):
        """Return the dict, tho"""
        return dir(self)