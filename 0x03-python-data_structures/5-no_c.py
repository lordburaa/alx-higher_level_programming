#!/usr/bin/python3
def no_c(my_string):
    k = 0
    j = 0
    new_string = []
    list_t = list(my_string.strip(""))
    for i in list_t:
        if i == 'c' or i == 'C':
            j += 1
            continue
        new_string[k] = list_t[j]
        k += k
        j += 1
    ' '.join(new_string)
    for i in new_string:
        print("{}".format(i))
