#!/usr/bin/python3
def element_at(my_list, idx):
    for x in range(len(my_list)):
        if idx > len(my_list) or idx < 0:
            return None
        if idx == x:
            print("{:d}".format(int(x)))
