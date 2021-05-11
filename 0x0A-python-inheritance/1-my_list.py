#!/usr/bin/python3
"""
Write a class My_List that inherits from list
Public instance meth: def print_sorted(self):
that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """Top shelf, have some class"""
    def __init__(self):
        """Superdot inits with parent parameters"""
        super().__init__()

    def print_sorted(self):
        """return the sorted list intake"""
        print(sorted(self))
        """print("{}".format(self.sort)) does not work tho?"""
