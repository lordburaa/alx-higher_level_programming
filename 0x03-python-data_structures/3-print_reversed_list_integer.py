#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    
    new_list = my_list
    for i in range(len(my_list) - 1, -1, 0 ):
        print("{:d}".format(new_list[i]))
