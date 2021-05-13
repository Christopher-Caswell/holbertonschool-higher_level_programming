#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Append new strings in location"""
    z = []
    with open(filename, 'r+') as x:
        """Read to new string"""
        for eachline in x:
            z.append(y)
            if search_string in eachline:
                """I love 'in' but do not like the .action format"""
                z.append(new_string)
    with open(filename, 'w+') as a:
        a.write("".join(y))
