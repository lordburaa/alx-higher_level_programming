#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    leng = len(my_list) - 1
    new_list = my_list
    for i in range(leng, -1, -1):
        print("{}".format(new_list[i]))
