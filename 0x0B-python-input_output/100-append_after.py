#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Append new strings in location"""
    z = []
    with open(filename, 'r') as x:
        """Read to new string"""
        for y in x.readlines():
            z.append(y)
            if search_string in y:
                """I love 'in' but do not like the .action format"""
                z.append(new_string)
    with open(filename, 'x') as x:
        x.write("".join(y))
