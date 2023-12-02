#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = list(my_list)
    leng = len(my_list)
    if (idx < 0 or idx >= leng):
        return new
    else:
        new[idx] = element
        return new
