#!/usr/bin/python3
def max_integer(my_list=[]):
    max_t = 0
    if (len(my_list) == 0):
        return None
    for i in range(len(my_list)):
        if (max_t >= my_list[i]):
            continue
        else:
            max_t = my_list[i]
    return max_t
