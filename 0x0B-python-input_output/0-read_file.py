#!/usr/bin/python3
"""
Write a function that reads a
text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """Prints a text read from a file"""
    with open(filename, encoding="UTF8") as x:
        print("".join(x.readlines()), end="")
