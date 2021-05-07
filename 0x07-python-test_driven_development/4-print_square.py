#!/usr/bin/python3
""""
Print My Square by Anita Ward
A beautiuful song that doesn't permit non ints
Any zeroes (or less) need not apply
"""


def print_square(size):
    """Sing that beautiful square footage"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end="")
    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
