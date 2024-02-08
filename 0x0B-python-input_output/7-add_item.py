#!/usr/bin/python3
"""
    json
"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item(args):
    """add all argument to a pyton list and save them to a file"""
    list_t=[]
    list_t=list(load_from_json_file("add_item.json"))
    for i in args:
        list_t.append(i)
    new = json.dumps(list_t)
    save_to_json_file(new, "add_item.json")
    print("item added succesfully")
args = sys.argv[1:]
add_item(args)
