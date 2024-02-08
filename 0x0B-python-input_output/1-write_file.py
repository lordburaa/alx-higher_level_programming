#!/usr/bin/python3
"""write to the file"""


def write_file(filename="", text=""):
    """write to the file even when file is not exist"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
