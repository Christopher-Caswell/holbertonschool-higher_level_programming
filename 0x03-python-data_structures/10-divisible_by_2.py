#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    lx = list()
    for x in my_list:
        if x % 2 == 0:
            lx.append(True)
        else:
            lx.append(False)
    return lx
