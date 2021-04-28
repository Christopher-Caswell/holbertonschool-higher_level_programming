#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        y = "arguments."
    elif len(argv) == 2:
        y = "argument:"
    else:
        y = "arguments:"
    print("{} {}".format(len(argv) - 1, (y)))
    for x in range(len(argv) - 1):
        print("{}: {}".format(x + 1, argv[x + 1]))
