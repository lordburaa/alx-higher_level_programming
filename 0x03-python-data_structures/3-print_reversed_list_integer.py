#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    leng = len(my_list)
    my_list.reverse()
    for i in range(leng):
        print("{}".format(my_list[i]))
