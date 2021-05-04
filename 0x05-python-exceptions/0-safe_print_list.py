#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if 0 < x < 6:
                print('{}'.format(my_list[:x]), end="")
        print('')
    except:
        print('{}'.format(my_list[x]))
    finally:
        return count
