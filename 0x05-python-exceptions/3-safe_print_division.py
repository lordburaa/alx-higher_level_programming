#!/usr/bin/python3
def safe_print_division(a, b):

    try:
        response = a / b
    except ZeroDivisionError:
        response = None
    finally:
        print('Insie result: {}'.format(response))

    return response
