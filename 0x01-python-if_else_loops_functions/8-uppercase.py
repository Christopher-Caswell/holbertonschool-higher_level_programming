#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        if ord(str[x]) > 96 and ord(str[x]) < 123:
            y = chr(ord(str[x]) - 32)
        else:
            y = str[x]
        print("{}".format(y), end="")
    print("")
