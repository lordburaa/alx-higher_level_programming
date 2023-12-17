#!/usr/bin/python3

def uniq_add(my_list=[]):
    a = set(my_list)
    sum_int = 0
    for i in a:
        sum_int += i
    return sum_int
