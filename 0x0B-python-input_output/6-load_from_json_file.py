#!/usr/bin/python3
""" json """


import json


def load_from_json_file(filename):
    """ loading form the file decode it"""

    with open(filename, 'r', encoding="utf-8") as f:
        new = f.read()
        objec = json.loads(new)
        return objec
