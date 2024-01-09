#!/usr/bin/python3
"""
    append the file 
"""


def append_write(filename="", text=""):
   """Appending the flile to the end of the file
   """

    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
