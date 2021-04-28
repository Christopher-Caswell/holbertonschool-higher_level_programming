#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    for x in range(len(dir(hidden_4))):
        if x[0] == '_' and x[1] == '_':
            continue
        else:
            print("{}".format(x))
