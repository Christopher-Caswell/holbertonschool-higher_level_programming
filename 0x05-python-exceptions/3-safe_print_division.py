#!/usr/bin/python3
def safe_print_division(a, b):
    if b == 0:
        result = None
        print("Inside Result: {}".format(result))
    try:
        result2 = a / b
        print("Inside result: {}".format(result2))
    except:
        result2 = None
    except not isinstance(b, int):
        result2 = None
    finally:
        return result2
