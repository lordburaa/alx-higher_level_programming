#!/usr/bin/python3
""" scripts for the json """


import sys
import json
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new = []
filename = "add_item.json"
if os.path.isfile(filename):
    load_from_json_file('add_item.json')

new.extend(sys.argv[1:])
save_to_json_file(new, filename)
