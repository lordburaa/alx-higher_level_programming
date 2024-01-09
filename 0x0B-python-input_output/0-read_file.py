#!/usr/bin/python3
"""
    read file 

"""


def read_file(filename=""):
    """
        read  file the file
        file already exit
    """

    with open(filename, 'r', encoding="utf-8") as f:
        read = f.readlines()
        print(read)
