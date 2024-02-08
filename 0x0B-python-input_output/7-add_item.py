#!/usr/bin/python3
"""
    json
"""
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item(filename, *args):
    """add all argument to a pyton list and save them to a file"""

    filename="add_item.json"
    l = load_from_json_file
    for i in args:
        l.append(i)

    save_to_file(l, filename)
