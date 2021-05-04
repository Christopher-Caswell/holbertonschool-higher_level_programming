#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
        y = 0
        for z in range(x):
            try:
                print('{:d}'.format(my_list[z]), end="")
                y += 1
            except (ValueError, TypeError):
                print("", end="")
        print("")
        return y
