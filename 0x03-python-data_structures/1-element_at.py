#!/usr/bin/python3
def element_at(my_list, idx):
    for x in range(len(my_list)):
        if idx == x:
            print("{}".format(x))
