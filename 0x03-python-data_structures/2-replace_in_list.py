#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    leng = len(my_list)
    if (idx < 0):
        return my_list
    if (idx >= leng - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list
