#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    
    if not my_list:
        return None
    new_list = my_list
    for i in range(len(my_list)):
        print("{:d}".format(new_list[i]))
    return new_list
