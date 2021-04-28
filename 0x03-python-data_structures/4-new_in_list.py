#!/usr/bin/python3
def new_in_list(my_list, idx, element): 
    if idx < 0 or idx > len(my_list):
        return my_list
    tmp = list()
    for x in range(len(my_list)):
        if x == idx:
            tmp.append(element)
        else:
            tmp.append(my_list[x])
    return tmp
