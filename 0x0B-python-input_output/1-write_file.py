#!/usr/bin/python3
"""
Write a function that writes a string to a text file
(UTF8) and returns the number of characters written
Your function should create the file if doesnt exist.
Your function should overwrite the content
of the file if it already exists.
"""


def write_file(filename="", text=""):
    """Write the file, silly naming convention"""
    with open(filename, 'w',  encoding="UTF8") as x:
        writ = x.write(text)
    return writ
