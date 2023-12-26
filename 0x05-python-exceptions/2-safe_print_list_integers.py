#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except SyntaxError as error:
            print("error")
    print()
    return x
