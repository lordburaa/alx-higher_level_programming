#!/usr/bin/python3
"""read file """

def read_file(filename=""):
    """Reading file from the file"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
