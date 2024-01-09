#!/usr/bin/python3
""" scripts for the json """


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new = sys.argv[1:]
with open('add_item.json', 'r') as r:

    save_to_json_file(new, 'add_item.json')

    pr = load_from_json_file('add_item.json')

    print(pr)
