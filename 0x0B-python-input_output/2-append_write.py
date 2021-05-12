#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text
file (UTF8) and returns the number of characters added
If the file doesnt exist, it should be created
"""


def append_write(filename="", text=""):
    """add stuff to the end, bruh"""
    with open(filename, 'a', encoding="UTF8") as x:
        return x.write(text)
