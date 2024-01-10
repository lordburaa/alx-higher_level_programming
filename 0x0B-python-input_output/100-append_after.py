#!/usr/bin/python3
""" module define a text file insertion """


def append_after(filename="", search_string="", new_string=""):
    """ insert """
    test = ""
    with open(filename) as r:
        for line in r:
            test += line
            if search_string in line:
                test += new_string
    with open(filename, 'w') as w:
        w.write(test)
