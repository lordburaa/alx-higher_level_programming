#!/usr/bin/python3
""" scripts for the json """


import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.isfile(filename):
    new = load_from_json_file(filename)
    print(new)
else:
    new = []
if sys.argv[1:]:
    new.extend(sys.argv[1:])
print("checking\t",new)
save_to_json_file(new, filename)
