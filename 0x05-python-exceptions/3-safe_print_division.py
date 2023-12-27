#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        c = a / b
    except (ZeroDivisionError, NameError) as ex:
        c = None
    finally:
        if c is None:
            print("Inside result: {}".format(c))
            return c
        else:
            print("Inside result: {}".format(c))
            return c
