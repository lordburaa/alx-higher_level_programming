#!/usr/bin/python3
def remove_char_at(str, n):
    ptr = str
    if (n >= 0):
        str = ptr[0:n] + ptr[n+1:]
    else:
        str = ptr[0:]
    return str
