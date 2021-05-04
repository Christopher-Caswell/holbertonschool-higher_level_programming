#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        _return = a / b
    except:
        _return = None
    finally:
        print("Inside result: {}".format(_return))
        return _return
