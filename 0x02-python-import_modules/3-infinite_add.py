#!/usr/bin/python3
if "__main__" == __name__:
    import sys
    y = 0
    for x in range(1, len(sys.argv)):
        y = int(sys.argv[x]) + y
print(y)
